from typing import List, Dict, Any
from matplotlib import pyplot as plt
import numpy as np
import sys
sys.path.append('./agents')
from bfs import BfsAgent
from dfs import DfsAgent
from ucs import UcsAgent
from map import Map 
from runAgent import runAgent

def generateBoxPlot():
    # Get Data
    dataObject: Dict[str, List[List[int]]] = getData()

    # List of keys to iterate through
    keys = ["totalCostArr", "exploredNodesArr", "timeTakenArr"]

    # Generates a box plot graph per variable to study
    for i in range(3):
        # Create dataset
        data1 = dataObject[keys[i]][0]
        data2 = dataObject[keys[i]][1]
        data3 = dataObject[keys[i]][2]
        data4 = dataObject[keys[i]][3]
        data5 = dataObject[keys[i]][4]
        data = [data1, data2, data3, data4, data5]

        # Ensure that data contains only numeric values
        data = [list(d) if isinstance(d, set) else d for d in data]

        # Calculates the mean and standard deviations for each dataset
        mean = [np.mean(d) if len(d) > 0 else float('nan') for d in data]  # Avoid empty lists
        std_devs = [np.std(d) if len(d) > 0 else float('nan') for d in data]  # Avoid empty lists


        # Creates a boxplot
        plt.boxplot(data, labels=['BFS Agent', 'DFS Agent', 'DFS Agent(md=100)', 'UCS Agent', 'UCS Agent(e2)'])

        # Adds mean as red dots
        for j in range(len(mean)):
            plt.plot(j + 1, mean[j], 'ro')

        # Adds standard deviations as error bars
        for j in range(len(std_devs)):
            plt.errorbar(j + 1, mean[j], yerr=std_devs[j], fmt='o', color='red')

        # Plots graph
        plt.title(f'{keys[i]} by Agent')
        plt.xlabel(keys[i])
        plt.ylabel('Value')
        plt.show()

def getData() -> Dict[str, List[List[int]]]:
    map = Map(100, 0.92)  # instance for runAgent()
    agents = [BfsAgent(), DfsAgent(), DfsAgent(10), UcsAgent(), UcsAgent(costByAction=True)]

    totalCostArr: List[List[int]] = [[] for _ in range(len(agents))]
    exploredNodesArr: List[List[int]] = [[] for _ in range(len(agents))]
    timeTakenArr: List[List[int]] = [[] for _ in range(len(agents))]

    # 30 iterations per Agent in new random 100x100 Map
    for idx, agent in enumerate(agents):
        for _ in range(30):
            response = runAgent(map, agent)
           
            if response:
                totalCost = response.get("totalCost", 0)
                exploredNodes = response.get("exploredNodes", 0)
                timeTaken = response.get("timeTaken", 0)
                totalCostArr[idx].append(totalCost)
                exploredNodesArr[idx].append(exploredNodes)
                timeTakenArr[idx].append(timeTaken)

    # Return a dictionary with all the data
    return {
        "totalCostArr": totalCostArr,
        "exploredNodesArr": exploredNodesArr,
        "timeTakenArr": timeTakenArr
    }
