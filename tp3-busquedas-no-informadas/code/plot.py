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


def generateCSV(data):

    # Nombres de los algoritmos
    algorithms = ['BFS', 'DFS', 'DFS (limit 10)', 'UCS', 'UCS (cost)', 'A*']
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
                totalCost = data["totalCost"][idx][env_n]
                exploredNodes = data["exploredNodes"][idx][env_n]
                timeTaken = data["timeTaken"][idx][env_n]
                solutionFound = data["solutionFound"][idx][env_n]

                # Escribe la fila con los datos en el CSV
                writer.writerow([
                    algorithm,           # algorithm_name
                    env_n + 1,           # env_n (1 a 30)
                    exploredNodes,       # states_n
                    # cost_e1 (coste total del escenario 1)
                    totalCost,
                    # cost_e2 (coste total del escenario 2)
                    totalCost,
                    timeTaken,           # time
                    solutionFound        # solution_found
                ])


def generateBoxPlot(dataObject):

    # List of keys to iterate through
    keys = ["totalCost", "exploredNodes", "timeTaken"]

    # Generates a box plot graph per variable to study
    for i in range(3):
        # Create dataset
        data1 = dataObject[keys[i]][0]
        data2 = dataObject[keys[i]][1]
        data3 = dataObject[keys[i]][2]
        data4 = dataObject[keys[i]][3]
        data5 = dataObject[keys[i]][4]
        data6 = dataObject[keys[i]][5]
        data = [data1, data2, data3, data4, data5, data6]

        # Ensure that data contains only numeric values
        data = [list(d) if isinstance(d, set) else d for d in data]

        # Calculates the mean and standard deviations for each dataset
        mean = [np.mean(d) if len(d) > 0 else float('nan')
                for d in data]  # Avoid empty lists
        std_devs = [np.std(d) if len(d) > 0 else float('nan')
                    for d in data]  # Avoid empty lists

        # Creates a boxplot
        plt.boxplot(data, labels=['BFS Agent', 'DFS Agent',
                    'DFS Agent(md=100)', 'UCS Agent', 'UCS Agent(e2)', 'A* Agent'])

        # Adds mean as red dots
        for j in range(len(mean)):
            plt.plot(j + 1, mean[j], 'ro')

        # Adds standard deviations as error bars
        for j in range(len(std_devs)):
            plt.errorbar(j + 1, mean[j],
                         yerr=std_devs[j], fmt='o', color='red')

        # Plots graph
        plt.title(f'{keys[i]} by Agent')
        plt.xlabel(keys[i])
        plt.ylabel('Value')
        plt.show()


def getData() -> Dict[str, List[List[int]]]:
    map = Map(100, 0.92)  # instance for runAgent()
    agents = [BfsAgent(), DfsAgent(), DfsAgent(
        10), UcsAgent(), UcsAgent(costByAction=True), AStarAgent()]

    totalCostArr: List[List[int]] = [[] for _ in range(len(agents))]
    exploredNodesArr: List[List[int]] = [[] for _ in range(len(agents))]
    timeTakenArr: List[List[int]] = [[] for _ in range(len(agents))]
    solutionFoundArr: List[List[int]] = [[] for _ in range(len(agents))]
    envSeedArr: List[List[int]] = [[] for _ in range(len(agents))]

    # 30 iterations per Agent in new random 100x100 Map
    for idx, agent in enumerate(agents):
        for _ in range(30):
            response = runAgent(map, agent)

            if response:
                totalCost = response.get("totalCost")
                exploredNodes = response.get("exploredNodes")
                timeTaken = response.get("timeTaken")
                solutionFound = response.get("solutionFound")
                envSeed = response.get("envSeed")
                totalCostArr[idx].append(totalCost)
                exploredNodesArr[idx].append(exploredNodes)
                timeTakenArr[idx].append(timeTaken)
                solutionFoundArr[idx].append(solutionFound)
                envSeedArr[idx].append(envSeed)

    # Return a dictionary with all the data
    return {
        "totalCost": totalCostArr,
        "exploredNodes": exploredNodesArr,
        "timeTaken": timeTakenArr,
        "solutionFound": solutionFoundArr,
        "envSeed": envSeedArr
    }
