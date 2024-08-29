import matplotlib.pyplot as plt
import numpy as np
from environment import Environment
from agents import RandomAgent, ReflexiveSimpleAgent
from main import iteration
from itertools import chain

# averagesR = []
# averagesS = []
# for dimension in dimensions:
#   for dirtRate in dirtRates:
#     averageR = []
#     averageS = []
#     for i in range(0,10,1):
#       env = Environment(dimension, dimension, dirtRate=dirtRate)
#       simpleAgent = ReflexiveSimpleAgent(env)

#       averageS.append(iteration(env, simpleAgent))

#     averagesS.append(np.average(averageS))


dimensions = [2,4,8,16,32,64,128]
dirtRates = [0.1,0.2,0.4,0.8]

averageR = [np.float64(11.8), np.float64(12.2), np.float64(35.7), np.float64(46.1), np.float64(163.0), np.float64(216.6), np.float64(423.0), np.float64(408.7), np.float64(2065.7), np.float64(1834.6), np.float64(2378.8), np.float64(2931.7), np.float64(10920.3), np.float64(11299.0), np.float64(15881.3), np.float64(14119.9), np.float64(67188.6), np.float64(73925.2), np.float64(79713.9), np.float64(88957.0), np.float64(297140.4), np.float64(328775.9), np.float64(412999.1), np.float64(462095.1), np.float64(1804445.5), np.float64(1861635.9), np.float64(1832543.6), np.float64(2128589.9)]
averageS = [np.float64(0.5), np.float64(2.6), np.float64(7.1), np.float64(9.4), np.float64(38.3), np.float64(93.7), np.float64(86.4), np.float64(102.0), np.float64(234.4), np.float64(458.2), np.float64(727.2), np.float64(697.3), np.float64(3411.6), np.float64(3938.8), np.float64(4970.0), np.float64(4677.4), np.float64(17428.6), np.float64(25116.7), np.float64(24540.5), np.float64(25190.5), np.float64(96325.0), np.float64(129468.8), np.float64(129363.3), np.float64(143894.1), np.float64(655578.7), np.float64(706062.6), np.float64(609527.9), np.float64(751177.1)]

for i in range(len(dimensions)):
    start_idx = i * 4
    end_idx = start_idx + 4
    arr1 = averageR[start_idx:end_idx]
    arr2 = averageS[start_idx:end_idx]
    
    y = list(chain.from_iterable(zip(arr1, arr2)))
    
    colors = ["#619cff", "#f8766d"] * 4
    fig, ax = plt.subplots()            
    ax.bar(["random 0.1", "simple 0.1", "random 0.2", "simple 0.2", "random 0.4", "simple 0.4", "random 0.8", "simple 0.8"], y, color=colors)  
    ax.set_title(f"Dimension {dimensions[i]}x{dimensions[i]}")
    plt.show()
