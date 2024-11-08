# Cargar librerías
library(tidyverse)
library(caret)
library(pROC)
library(xgboost)
library(doParallel)

# Configurar paralelismo
registerDoParallel(cores = detectCores() - 1)

# Cargar los datos
train_set <- read.csv("tp7-ml/code/desafio/arbolado-mza-dataset.csv")
test_data <- read.csv("tp7-ml/code/desafio/arbolado-mza-dataset-test.csv")

# Convertir 'inclinacion_peligrosa' a binaria y factor con nombres válidos
train_set$inclinacion_peligrosa <- factor(train_set$inclinacion_peligrosa, levels = c(0, 1), labels = c("No", "Sí"))

# Identificar las variables numéricas en el conjunto de entrenamiento y prueba
num_vars_train <- names(train_set)[sapply(train_set, is.numeric)]
num_vars_test <- names(test_data)[sapply(test_data, is.numeric)]
num_vars_common <- intersect(num_vars_train, num_vars_test)

# Normalizar variables numéricas
train_set_numeric <- train_set[, num_vars_common] %>%
  mutate(across(everything(), ~ ( . - min(.)) / (max(.) - min(.))))
test_data_numeric <- test_data[, num_vars_common] %>%
  mutate(across(everything(), ~ ( . - min(train_set_numeric[[cur_column()]])) / (max(train_set_numeric[[cur_column()]]))))

# Selección de características con RFE
control <- rfeControl(functions = rfFuncs, method = "cv", number = 5, allowParallel = TRUE)
features <- rfe(train_set_numeric, train_set$inclinacion_peligrosa, sizes = c(5, 10, 15), rfeControl = control)
selected_vars <- features$optVariables

# Filtrar conjuntos con características seleccionadas
train_set_selected <- train_set_numeric[, selected_vars]
test_set_selected <- test_data_numeric[, selected_vars]

# Crear matrices DMatrix para XGBoost
train_matrix <- xgb.DMatrix(data = as.matrix(train_set_selected), label = as.numeric(train_set$inclinacion_peligrosa) - 1)
test_matrix <- xgb.DMatrix(data = as.matrix(test_set_selected))

# Búsqueda de hiperparámetros (grid search)
tune_grid <- expand.grid(
  nrounds = c(50, 100, 150),
  max_depth = c(3, 6, 9),
  eta = c(0.01, 0.1, 0.3),
  gamma = c(0, 1, 5),
  colsample_bytree = c(0.6, 0.8, 1.0),
  min_child_weight = c(1, 5, 10),
  subsample = c(0.6, 0.8, 1.0)  # Agregar el parámetro subsample
)

train_control <- trainControl(
  method = "cv", 
  number = 5,
  classProbs = TRUE,
  summaryFunction = twoClassSummary,
  allowParallel = TRUE
)

# Convertir 'inclinacion_peligrosa' a factor para entrenar con caret
xgb_tuned <- train(
  x = as.matrix(train_set_selected), 
  y = factor(train_set$inclinacion_peligrosa, levels = c("No", "Sí")),
  method = "xgbTree",
  metric = "ROC",
  tuneGrid = tune_grid,
  trControl = train_control
)

# Obtener mejores hiperparámetros
best_params <- xgb_tuned$bestTune
params <- list(
  objective = "binary:logistic",
  eval_metric = "auc",
  max_depth = best_params$max_depth,
  eta = best_params$eta,
  gamma = best_params$gamma,
  colsample_bytree = best_params$colsample_bytree,
  min_child_weight = best_params$min_child_weight,
  scale_pos_weight = sum(train_set$inclinacion_peligrosa == "No") / sum(train_set$inclinacion_peligrosa == "Sí"),
  subsample = best_params$subsample  # Añadir el parámetro subsample
)

# Entrenamiento con mejores hiperparámetros
xgb_model <- xgboost(params = params, data = train_matrix, nrounds = best_params$nrounds, verbose = 0)

# Predicciones en el conjunto de prueba
val_preds <- predict(xgb_model, test_matrix)

# Determinar umbral óptimo
optimal_cutoff <- coords(roc(as.numeric(train_set$inclinacion_peligrosa) - 1, predict(xgb_model, train_matrix)), "best", ret = "threshold")

# Clasificar con el umbral óptimo
test_preds <- ifelse(val_preds > optimal_cutoff, 1, 0)

# Crear archivo de envío
submission <- data.frame(
  ID = test_data$id,
  inclinacion_peligrosa = test_preds
)
write.csv(submission, "tp7-ml/code/desafio/arbolado-mza-dataset-envio.csv", row.names = FALSE)
