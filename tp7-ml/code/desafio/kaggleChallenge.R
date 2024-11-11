# Cargar librerías necesarias
library(dplyr)
library(DMwR)
library(ROSE)
library(randomForest)
library(e1071)
library(caret)
library(pROC)

# Filtra las especies raras en el dataset
remove_rare_species <- function(data, min_count = 100) {
  species_counts <- data %>%
    count(especie) %>%
    filter(n >= min_count)
  
  filtered_data <- data %>%
    filter(especie %in% species_counts$especie)
  
  return(filtered_data)
}

# Realiza oversampling usando SMOTE o ROSE
# Función para realizar oversampling con variables categóricas
perform_oversampling <- function(data, method = "SMOTE") {
  data$inclinacion_peligrosa <- as.factor(data$inclinacion_peligrosa)
  
  # Convertir variables categóricas en dummy variables (one-hot encoding)
  dummies_model <- dummyVars(inclinacion_peligrosa ~ ., data = data)
  data_dummies <- predict(dummies_model, newdata = data) %>% as.data.frame()
  data_dummies$inclinacion_peligrosa <- data$inclinacion_peligrosa
  
  if (method == "SMOTE") {
    # Aplicar SMOTE
    balanced_data <- DMwR::SMOTE(inclinacion_peligrosa ~ ., data = data_dummies)
  } else if (method == "ROSE") {
    # Aplicar ROSE
    balanced_data <- ROSE::ovun.sample(
      inclinacion_peligrosa ~ .,
      data = data_dummies,
      method = "over",
      N = max(2 * nrow(data_dummies), nrow(data_dummies))
    )$data
  } else {
    stop("El método debe ser 'SMOTE' o 'ROSE'")
  }
  
  return(balanced_data)
}

# Realiza undersampling usando ROSE
perform_undersampling <- function(data) {
  data$inclinacion_peligrosa <- as.factor(data$inclinacion_peligrosa)
  min_class_size <- min(table(data$inclinacion_peligrosa))
  
  balanced_data <- ROSE::ovun.sample(
    inclinacion_peligrosa ~ .,
    data = data,
    method = "under",
    N = 2 * min_class_size
  )$data
  
  return(balanced_data)
}

# Crea un clasificador Random Forest
random_forest_classifier <- function(train_data, ntree = 500, mtry = NULL) {
  train_data$inclinacion_peligrosa <- as.factor(train_data$inclinacion_peligrosa)
  
  rf_model <- randomForest(
    inclinacion_peligrosa ~ altura + circ_tronco_cm + diametro_tronco + especie + seccion,
    data = train_data,
    importance = TRUE,
    ntree = ntree,
    mtry = mtry
  )
  
  return(rf_model)
}

# Realiza predicciones con el modelo Random Forest
predict_random_forest <- function(rf_model, validation_data) {
  predictions_prob <- predict(rf_model, validation_data, type = "prob")
  
  result <- data.frame(
    id = validation_data$id,
    inclinacion_peligrosa = predictions_prob[, "1"]
  )
  
  return(result)
}

# Entrena el modelo de ensamble con Random Forest y SVM
train_ensemble_model <- function(datos, target_var, predictors, ntree = 1000, mtry = 5, cost = 20, gamma = 0.1) {
  datos[[target_var]] <- as.factor(datos[[target_var]])
  
  set.seed(2001)
  index <- createDataPartition(datos[[target_var]], p = .8, list = FALSE)
  train_data <- datos[index, ]
  
  rf_model <- randomForest(
    as.formula(paste(target_var, "~", paste(predictors, collapse = "+"))),
    data = train_data,
    ntree = ntree,
    mtry = mtry
  )
  
  svm_model <- svm(
    as.formula(paste(target_var, "~", paste(predictors, collapse = "+"))),
    data = train_data,
    cost = cost,
    gamma = gamma,
    kernel = "sigmoid"
  )
  
  return(list(rf_model = rf_model, svm_model = svm_model))
}

# Predice usando el modelo de ensamble y aplica votación mayoritaria
predict_with_ensemble <- function(models, new_data) {
  if (!"id" %in% colnames(new_data)) {
    stop("El nuevo dataset debe contener la columna 'id'.")
  }
  
  rf_pred <- predict(models$rf_model, newdata = new_data)
  svm_pred <- predict(models$svm_model, newdata = new_data)
  
  combined_predictions <- data.frame(rf_pred, svm_pred)
  
  final_pred_values <- apply(combined_predictions, 1, function(x) {
    as.character(names(sort(table(x), decreasing = TRUE)[1]))
  })
  
  final_pred <- data.frame(id = new_data$id, inclinacion_peligrosa = final_pred_values)
  
  return(final_pred)
}

# Evalúa el modelo utilizando métricas como la matriz de confusión y AUC-ROC
evaluate_model <- function(predictions, actual_values) {
  actual_values <- as.factor(actual_values)
  predictions <- as.factor(predictions)
  
  confusion_matrix <- confusionMatrix(predictions, actual_values)
  auc_roc <- roc(actual_values, as.numeric(predictions))
  
  list(
    confusion_matrix = confusion_matrix,
    auc_roc = auc_roc$auc
  )
}

