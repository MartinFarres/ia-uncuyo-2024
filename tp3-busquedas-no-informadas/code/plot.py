import csv
from map import Map
from runAgent import runAgent
from ucs import UcsAgent
from dfs import DfsAgent
from bfs import BfsAgent
from aStar import AStarAgent
from typing import List, Dict
from matplotlib import pyplot as plt
import numpy as np
import sys
sys.path.append('./agents')


def getGraphsAndTable():
    # Get Data
    dataObject: Dict[str, List[List[int]]] = getData()
    generateCSV(dataObject)
    generateBoxPlot(dataObject)
    generateBarChartForSolutions(dataObject)


def generateCSV(data):

    # Nombres de los algoritmos
    algorithms = ['BFS', 'DFS', 'DFS (limit 10)', 'UCS', 'A*']
    csv_file = 'informada-results.csv'

    # Abre el archivo CSV para escribir los datos
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Escribe los encabezados del CSV
        writer.writerow([
            'algorithm_name', 'env_n', 'states_n',
            'cost_e1', 'cost_e2', 'time', 'solution_found'
        ])

        # Recorre los datos de cada algoritmo
        for idx, algorithm in enumerate(algorithms):
            # Para cada entorno generado aleatoriamente (hay 30)
            for env_n in range(30):
                costE1 = data["costE1"][idx][env_n]
                costE2 = data["costE2"][idx][env_n]
                exploredNodes = data["exploredNodes"][idx][env_n]
                timeTaken = data["timeTaken"][idx][env_n]
                solutionFound = data["solutionFound"][idx][env_n]

                # Escribe la fila con los datos en el CSV
                writer.writerow([
                    algorithm,           # algorithm_name
                    env_n + 1,           # env_n (1 a 30)
                    exploredNodes,       # states_n
                    # cost_e1 (coste total del escenario 1)
                    costE1,
                    # cost_e2 (coste total del escenario 2)
                    costE2,
                    timeTaken,           # time
                    solutionFound        # solution_found
                ])


def generateBoxPlot(dataObject):

    # List of keys to iterate through
    keys = ["costE1", "costE2", "exploredNodes", "timeTaken"]

    # Generate box plot graph per variable
    for i in range(4):
        data_filtered = []

        # Iterate through each agent's data
        for idx in range(5):  # 5 agents (BFS, DFS, DFS (limit 10), UCS, A*)
            # Filter data where the solution was found (solutionFound == True)
            filtered_data = [dataObject[keys[i]][idx][j]
                             for j in range(30)
                             if dataObject["solutionFound"][idx][j] == True]

            data_filtered.append(filtered_data)

        # Ensure that data contains only numeric values and avoid empty lists
        data_filtered = [list(d) if isinstance(
            d, set) else d for d in data_filtered]

        # Calculate the mean and standard deviations for each dataset
        mean = [np.mean(d) if len(d) > 0 else float('nan')
                for d in data_filtered]
        std_devs = [np.std(d) if len(d) > 0 else float('nan')
                    for d in data_filtered]

        # Create the boxplot
        plt.boxplot(data_filtered, labels=[
                    'BFS Agent', 'DFS Agent', 'DFS Agent (limit 10)', 'UCS Agent', 'A* Agent'])

        # Add mean as red dots
        for j in range(len(mean)):
            plt.plot(j + 1, mean[j], 'ro')

        # Add standard deviations as error bars
        for j in range(len(std_devs)):
            plt.errorbar(j + 1, mean[j],
                         yerr=std_devs[j], fmt='o', color='red')

        # Plot the graph
        plt.title(f'{keys[i]} by Agent')
        plt.xlabel(keys[i])
        plt.ylabel('Value')
        plt.show()


def generateBarChartForSolutions(dataObject):
    # Lista de algoritmos a analizar
    algorithms = ['BFS', 'DFS', 'DFS (limit 10)', 'UCS', 'A*']

    # Crear dataset para contar cuántas veces cada algoritmo llegó al objetivo
    solutions_count = []
    for idx in range(len(algorithms)):
        count_solutions = sum(
            1 for cost in dataObject["costE1"][idx] if cost != 0)
        solutions_count.append(count_solutions)

    # Crear gráfico de barras
    plt.bar(algorithms, solutions_count, color='skyblue')

    # Etiquetas y título del gráfico
    plt.title('Cantidad de veces que cada algoritmo llegó al objetivo')
    plt.xlabel('Algoritmos')
    plt.ylabel('Cantidad de soluciones encontradas')

    # Mostrar el gráfico
    plt.show()


def getData() -> Dict[str, List[List[int]]]:
    map = Map(100, 0.92)  # instance for runAgent()
    agents = [BfsAgent(), DfsAgent(), DfsAgent(
        10), UcsAgent(), AStarAgent()]

    costE1Arr: List[List[int]] = [[] for _ in range(len(agents))]
    costE2Arr: List[List[int]] = [[] for _ in range(len(agents))]
    exploredNodesArr: List[List[int]] = [[] for _ in range(len(agents))]
    timeTakenArr: List[List[int]] = [[] for _ in range(len(agents))]
    solutionFoundArr: List[List[int]] = [[] for _ in range(len(agents))]
    envSeedArr: List[List[int]] = [[] for _ in range(len(agents))]

    # 30 iterations per Agent in new random 100x100 Map
    for idx, agent in enumerate(agents):
        for _ in range(30):
            response = runAgent(map, agent)

            if response:
                costE1 = response.get("costE1")
                costE2 = response.get("costE2")
                exploredNodes = response.get("exploredNodes")
                timeTaken = response.get("timeTaken")
                solutionFound = response.get("solutionFound")
                envSeed = response.get("envSeed")
                costE1Arr[idx].append(costE1)
                costE2Arr[idx].append(costE2)
                exploredNodesArr[idx].append(exploredNodes)
                timeTakenArr[idx].append(timeTaken)
                solutionFoundArr[idx].append(solutionFound)
                envSeedArr[idx].append(envSeed)

    # Return a dictionary with all the data
    return {
        "costE1": costE1Arr,
        "costE2": costE2Arr,
        "exploredNodes": exploredNodesArr,
        "timeTaken": timeTakenArr,
        "solutionFound": solutionFoundArr,
        "envSeed": envSeedArr
    }
