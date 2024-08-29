# Respuestas Preguntas TP3

## Ejercicio 4

### La función make tiene como argumento is_slippery. ¿Qué controla dicho argumento?¿Cuál es su valor por defecto?

El valor **_is_slippery_** controla si el jugador se mueve a la cuadrilla deseada. Si el valor el **True**, solo se movera un 1/3 de las veces en la direccion seleccionada. Su valor por defecto es **False**.

### ¿Cómo son los entornos anteriores? Describa el tamaño, cantidad de agujeros, posición inicial del agente y del objetivo.

Los entornos definidos por **_map_name_** son mapas predeterminados con un cierto tamaño, cantidad de aguejor, posicion inicial del agente y del objetivo. Si se utiliza el parametro **desc** se puede establecer las condiciones del mapa que uno desee siguiendo los siguientes parametros:

- **S**: Posicion Inicial de agente,
- **F**: La celda es nieve (puede ser caminada),
- **H**: La celda es hielo (al pisar el agente pierde),
- **G**: Posicion del Objetivo.

Mientras que si se utiliza la funcion **_generate_random_map_**, se obtienen entornos aleatorios del tamaño deseado; pero, las posiciones inicial del agente y del objetivo permanecen iguales.
