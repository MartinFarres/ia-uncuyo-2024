from typing import List
from matplotlib import pyplot as plt
import numpy as np
# Local Imports -----------
from bfs import BfsAgent
from dfs import DfsAgent
from ucs import UcsAgent
from map import Map
from main import runAgent
# -------------------------

def generateBoxPlot():
  # Get Data
  dataObject:object = getData()
  
  # List of keys to iterate through
  keys = ["totalCostArr", "totalCostByActionArr", "exploredNodesArr", "timeTakenArr"]

  # Generates a box plot graph per variable to study
  for i in range(0,4):
    # Creates dataset
    data1 = dataObject[keys[i]][0]
    data2 = dataObject[keys[i]][1] 
    data3 = dataObject[keys[i]][2]
    data4 = dataObject[keys[i]][3]
    data = data1 + data2 + data3 + data4

    # Calculates the mean and standard deviations
    mean = [np.mean(d) for d in data]
    std_devs = [np.std(d) for d in data]
    
    # Creates a boxplot
    plt.boxplot(data, labels=['BFS Agent', 'DFS Agent', 'DFS Agent(md=100)', 'UCS Agent'])
    
    # Adds mean as red dots
    for i in range(len(mean)):
      plt.plot(i + 1, mean[i], 'ro')
    
    # Adds standard deviations as error bars
    for i in range(len(std_devs)):
      plt.errorbar(i + 1, mean[i], yerr=std_devs[i], fmt='o', color='red')
    
    # Plots graph
    plt.title(keys[i], " By Agent")
    plt.xlabel(keys[i])
    plt.ylabel('Value')
    plt.show()

    
def getData()->object:
  map = Map(100, 0.92) # Only for instancing the agents
  agents = [BfsAgent(map), DfsAgent(map), DfsAgent(map, 10), UcsAgent(map)]

  totalCostArr:List[List[int]] = [[]]
  totalCostByActionArr:List[List[int]] = [[]]
  exploredNodesArr:List[List[int]] = [[]]
  timeTakenArr:List[List[int]] = [[]]
  
  # 30 iterations per Agent in new random 100x100 Map
  for idx, agent in agents:
    for _ in range(0, 30, 1):
      totalCost, totalCostByAction, exploredNodes, timeTaken = runAgent(map, agent)

      totalCostArr[idx].append(totalCost)
      totalCostByActionArr[idx].append(totalCostByAction)
      exploredNodesArr[idx].append(exploredNodes)
      timeTakenArr[idx].append(timeTaken)

  # { "totalCostArr": [[bfsAgentData], [dfsAgentData]...], 
  #   "totalCostByActionArr": [[bfsAgentData], [dfsAgentData]...],  
  # ... }
  return {totalCostArr, totalCostByActionArr, exploredNodesArr, timeTakenArr} 






