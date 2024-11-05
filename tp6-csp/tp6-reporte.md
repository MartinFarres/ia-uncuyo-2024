### 1. Describir en detalle una formulación CSP para el Sudoku.

- Variables: {c00, c01, ..., cij, ..., c88}
- Dominios: Dij={1, ..., 9}.
- Restricciones: un número solamente puede aparecer una vez
  - en cada fila
  - en cada columna
  - en cada región

### 2. Utilizar el algoritmo AC-3 para demostrar que la arco consistencia puede detectar la inconsistencia de la asignación parcial {WA=red, V=blue} para el problema de colorear el mapa de Australia (Figura 5.1 AIMA 2da edición).

### Solución con AC-3 para detectar inconsistencia en la asignación parcial

**Asignación parcial inicial:**

- \( WA = \text{red} \)
- \( V = \text{blue} \)

**Dominios iniciales de los otros estados:**

- \( NT = \{ \text{red}, \text{green}, \text{blue} \} \)
- \( SA = \{ \text{red}, \text{green}, \text{blue} \} \)
- \( Q = \{ \text{red}, \text{green}, \text{blue} \} \)
- \( NSW = \{ \text{red}, \text{green}, \text{blue} \} \)

**Paso 1: Propagación de restricciones**

- Eliminar **red** de \( NT \) y \( SA \) (por \( WA = \text{red} \)).
- Eliminar **blue** de \( SA \) y \( NSW \) (por \( V = \text{blue} \)).

**Dominios actualizados:**

- \( NT = \{ \text{green}, \text{blue} \} \)
- \( SA = \{ \text{green} \} \)
- \( Q = \{ \text{red}, \text{green}, \text{blue} \} \)
- \( NSW = \{ \text{red}, \text{green} \} \)

**Paso 2: Revisión de arcos**

- \( SA \) solo puede ser **green**, lo que implica:
  - Eliminar **green** de \( NT \) y \( NSW \).

**Dominios actualizados:**

- \( NT = \{ \text{blue} \} \)
- \( NSW = \{ \text{red} \} \)

**Paso 3: Detección de inconsistencia**

- \( NT \) solo puede ser **blue**, lo que implica eliminar **blue** de \( Q \).
- Si \( Q \) se revisa, su dominio queda \( \{ \text{red}, \text{green} \} \).

**Resultado:**
El algoritmo AC-3 muestra que, al propagar las restricciones, no todos los estados pueden asignarse de forma consistente. La asignación parcial \( WA = \text{red} \) y \( V = \text{blue} \) es inconsistente porque los dominios de algunos estados se reducen de forma que violan las restricciones de adyacencia.

### **3. ¿Cuál es la complejidad en el peor caso cuando se ejecuta AC-3 en un árbol estructurado CSP? (i.e. cuando el grafo de restricciones forma un árbol: cualquiera dos variables están relacionadas por a lo sumo un camino).**

En el caso de un CSP estructurado como un árbol:

- E es el número de arcos (o restricciones) en el grafo.
- D es el tamaño del dominio más grande de las variables.

Por lo tanto, la complejidad en el peor caso de AC-3 en un CSP con estructura de árbol es O(ED)

Esto se debe a que cada arco es revisado como máximo una vez, y para cada arco, la verificación de consistencia entre los valores de los dominios de las variables involucradas toma (O(D)) tiempo.

### **4. AC-3 coloca de nuevo en la cola todo arco (Xk,Xi) cuando cualquier valor es removido del dominio de Xi incluso si cada valor de Xk es consistente con los valores restantes de Xi. Supongamos que por cada arco (Xk,Xi) se puede llevar la cuenta del número de valores restantes de Xi que sean consistentes con cada valor de Xk. Explicar cómo actualizar ese número de manera eficiente y demostrar que la arco consistencia puede lograrse en un tiempo total O(n^2.d^2).**

La idea básica es preprocesar las restricciones de manera que, para cada valor de Xi, llevemos un registro de aquellas variables Xk para las cuales un arco de Xk a Xi es satisfecho por ese valor particular de Xi. Esta estructura de datos puede calcularse en un tiempo proporcional al tamaño de la representación del problema. Luego, cuando se elimina un valor de Xi, reducimos en 1 el conteo de valores permitidos para cada arco (Xk, Xi) registrado bajo ese valor.

### Descripción del proceso:

1. **Preprocesamiento de restricciones**:

   - Para cada valor de una variable X_i, mantenemos un registro de las variables X_k cuyos arcos hacia X_i son consistentes con ese valor particular de X_i.
   - Este preprocesamiento permite que, cuando eliminemos un valor de X_i, sepamos qué arcos se ven afectados.

2. **Actualización eficiente**:
   - Cada vez que se elimina un valor del dominio de X_i, reducimos en 1 el conteo de los valores permitidos para cada variable X_k que depende de X_i, usando la estructura de datos previamente calculada.
   - Al mantener este registro, evitamos la necesidad de volver a verificar cada arco desde cero, lo que hace que la actualización sea más eficiente.

### Complejidad total \(O(n^2d^2)\):

- n es el número de variables y d es el tamaño del dominio más grande.
- Para cada par de variables, hay a lo sumo d^2 pares de valores a verificar, ya que para cada valor de X_i, tenemos que asegurarnos de que haya un valor en X_k que sea consistente.
- Este enfoque asegura que el algoritmo de consistencia de arcos se ejecute en tiempo total O(n^2d^2), ya que el preprocesamiento y las actualizaciones se realizan de manera eficiente en términos del número de arcos y valores posibles.

Este enfoque optimiza la verificación de consistencia de arcos al reducir la cantidad de verificaciones necesarias después de eliminar valores, al mantener actualizados los conteos de valores consistentes entre las variables relacionadas.

### 5. Demostrar la correctitud del algoritmo CSP para árboles estructurados (sección 5.4, p. 172 AIMA 2da edición). Para ello, demostrar:

a. Que para un CSP cuyo grafo de restricciones es un árbol, 2-consistencia (consistencia de arco) implica n-consistencia (siendo n número total de variables)

b. Argumentar por qué lo demostrado en a. es suficiente.

**Demostración:**

Supongamos que tenemos un CSP cuyo grafo de restricciones es un árbol y hemos logrado la 2-consistencia. Esto significa que para cada par de variables (Xi, Xj) en el CSP, cualquier valor en el dominio de Xi es consistente con al menos un valor en el dominio de Xj, y viceversa.

Para demostrar la n-consistencia, consideremos cualquier variable Xi en el CSP. Dado que el grafo de restricciones es un árbol, Xi está relacionada con el resto de las variables a través de un único camino en el árbol. Denotemos las variables en este camino como X1, X2, ..., Xn, donde X1 = Xi.

Dado que hemos logrado la 2-consistencia, sabemos que para cualquier variable Xk en el camino (donde k > 1), hay al menos un valor en el dominio de Xk que es consistente con algún valor en el dominio de Xk-1. Esto es cierto para todas las variables en el camino.

Por lo tanto, hemos demostrado que para cualquier variable Xi en el CSP, cualquier valor en su dominio es consistente con al menos un valor en el dominio de cada otra variable en el CSP, siguiendo el único camino en el árbol de restricciones.

Este resultado es suficiente porque, en un CSP, el objetivo es encontrar una asignación que cumpla con todas las restricciones. Si hemos logrado que todas las variables sean consistentes entre sí, hemos eliminado cualquier conflicto y hemos asegurado que existe una solución que satisface todas las restricciones. Esto es fundamental para la correctitud del algoritmo CSP en árboles estructurados, ya que garantiza que si una solución existe, el algoritmo la encontrará.
