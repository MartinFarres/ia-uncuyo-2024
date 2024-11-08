## **Resultados de la evaluación en tennis.csv**

Los resultados obtenidos se pueden apreciar en el siguiente diccionario:

{
'outlook': {
'overcast': 'yes',
'rainy': {
'windy': {np.False*: 'yes', np.True*: 'no'}
},
'sunny': {
'humidity': {'high': 'no', 'normal': 'yes'}
}
}
}

Básicamente, expresado en reglas significa que

- Si outlook = **overcast**, entonces play = yes.
- Si outlook = **rainy** y windy = **False**, entonces play = yes.
- Si outlook = **rainy** y windy = **True**, entonces play = no.
- Si outlook = **sunny** y humidity = **high**, entonces play = no.
- Si outlook = **sunny** y humidity = **normal**, entonces play = yes.

## **Información sobre las estrategias para datos de tipo real**

Cuando los datos contienen atributos **numéricos o continuos** (por ejemplo, edad, peso, o temperatura), los árboles de decisión adoptan estrategias específicas para dividir los datos en cada nodo. A continuación se describen las estrategias más comunes:

---

### **1. Divisiones Binarias con Umbral Óptimo**

- El árbol selecciona un **umbral de división** para cada atributo continuo, por ejemplo:  
  _¿Edad ≤ 30?_
- Para encontrar el mejor umbral, se prueban múltiples valores posibles y se elige el que maximiza alguna métrica (como **Ganancia de Información** o **Índice Gini**).
- Esto convierte el atributo continuo en dos ramas: una para los datos menores o iguales al umbral, y otra para los datos mayores.

**Ejemplo:**  
Si el umbral para "peso" es 70 kg, el nodo se dividirá en dos:

- Rama izquierda: individuos con peso ≤ 70 kg
- Rama derecha: individuos con peso > 70 kg

---

### **2. Estrategias Recursivas de Partición**

- Una vez que se hace la primera partición, cada subconjunto resultante vuelve a ser analizado recursivamente. Este proceso continúa hasta que se cumplan los criterios de parada (como alcanzar una profundidad máxima o que todas las instancias sean del mismo tipo).

---

### **3. Utilización de la Ganancia de Información y el Índice Gini**

- Para decidir qué atributo dividir y en qué punto, se usan métricas como:
  - **Ganancia de Información**: mide cuánto se reduce la incertidumbre después de la división.
  - **Índice Gini**: mide cuán "puras" son las nuevas ramas, es decir, si todas las instancias de una rama pertenecen a la misma clase.

---

### **4. Manejo de Overfitting**

- Dado que los atributos continuos pueden generar muchas divisiones, es fácil que el modelo sobreajuste. Por eso, se implementan **poda de árboles** (pruning) o límites en la profundidad del árbol para evitar este problema.

---
