import matplotlib.pyplot as plt
import seaborn as sns
import time
import pandas as pd


class PlotUtils:

    @staticmethod
    def generateResults(sizes, iterations, algorithm):
        # Crear una lista para almacenar los resultados
        resultados = []

        for size in sizes:
            print(f"\nProbando con un tablero de {size} reinas: ")

            # Variables para estadísticas
            for _ in range(iterations):
                # Medir tiempo de ejecución
                start_time = time.time()

                # Aplicar Algoritmo
                solucion, conflictos, estados = algorithm(size)

                # Medir tiempo final de ejecución
                end_time = time.time()
                tiempo_ejecucion = end_time - start_time

                # Almacenar resultados en la lista
                resultados.append({
                    "Tamaño del tablero": size,
                    "Tablero solución": solucion,
                    "Número de conflictos": conflictos,
                    "Estados explorados": estados,
                    "Tiempo (segundos)": tiempo_ejecucion,
                })

        return resultados

    @staticmethod
    def plot_tiempos(resultados_backtracking, resultados_forward):
        # Extraer tamaños y tiempos para backtracking
        sizes_backtracking = [r["Tamaño del tablero"]
                              for r in resultados_backtracking]
        tiempos_backtracking = [r["Tiempo (segundos)"]
                                for r in resultados_backtracking]

        # Extraer tamaños y tiempos para forward checking
        sizes_forward = [r["Tamaño del tablero"] for r in resultados_forward]
        tiempos_forward = [r["Tiempo (segundos)"] for r in resultados_forward]

        plt.figure(figsize=(12, 6))
        # Usar sizes_backtracking ya que asumo que ambos deben ser iguales
        sns.lineplot(x=sizes_backtracking, y=tiempos_backtracking,
                     label='Backtracking', marker='o', linestyle='--')
        sns.lineplot(x=sizes_forward, y=tiempos_forward,
                     label='Forward Checking', marker='o', linestyle='--')

        # Asegurarse de que todos los tamaños se muestran en el eje X
        plt.xticks(sizes_backtracking)
        plt.title('Comparación de Tiempos de Ejecución')
        plt.xlabel('Tamaño del tablero')
        plt.ylabel('Tiempo (segundos)')
        plt.legend()
        plt.grid()
        plt.show()

    @staticmethod
    def plot_estados(resultados_backtracking, resultados_forward):
        # Extraer tamaños y estados para backtracking
        sizes_backtracking = [r["Tamaño del tablero"]
                              for r in resultados_backtracking]
        estados_backtracking = [r["Estados explorados"]
                                for r in resultados_backtracking]

        # Extraer tamaños y estados para forward checking
        sizes_forward = [r["Tamaño del tablero"] for r in resultados_forward]
        estados_forward = [r["Estados explorados"] for r in resultados_forward]

        plt.figure(figsize=(12, 6))
        # Usar sizes_backtracking ya que asumo que ambos deben ser iguales
        sns.lineplot(x=sizes_backtracking, y=estados_backtracking,
                     label='Backtracking', marker='o', linestyle='--')
        sns.lineplot(x=sizes_forward, y=estados_forward,
                     label='Forward Checking', marker='o', linestyle='--')

        # Asegurarse de que todos los tamaños se muestran en el eje X
        plt.xticks(sizes_backtracking)
        plt.title('Comparación de Estados Explorados')
        plt.xlabel('Tamaño del tablero')
        plt.ylabel('Estados explorados')
        plt.legend()
        plt.grid()
        plt.show()
