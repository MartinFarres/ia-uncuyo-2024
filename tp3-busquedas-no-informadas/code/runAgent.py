import time
import sys
sys.path.append('./agents')
from agent import Agent
from map import Map
from gymnasium import wrappers
from dfs import DfsAgent

# Recommendation: Comment Print & UI sections for bulk runs 
def runAgent(map:Map, agent: Agent):
    # Env Definitions & Clean state
    map.generateMap()
    # nuevoLimite = 1000
    # env = wrappers.TimeLimit(map.env, nuevoLimite)
    env = map.env
    state = env.reset()

    # Get Time
    startTime = time.time()
    agent.searchAlgorithm(map)
    endTime = time.time() - startTime
    
    # Print
    # print(map.desc)
    # if len(agent.actionsList) > 0:
    #     print("Action List: ", agent.actionsList)
    #     print("Explored Node: ", len(agent.explored))
    #     print("Time Taken: ", endTime)
    # else:
    #     print("Goal not achieved")

    # UI
    # done = truncated = False
    # while not (done or truncated):
    #     try:
    #         action = agent.actionsList.pop(0)
    #     except Exception as err:  # Catch all exceptions
    #         raise Exception(f"An error occurred: {err}")
    #     next_state, reward, done, truncated, info = env.step(action)
    #     state = next_state
    env.close()
    response = {"totalCost": agent.calculateCost(), 
            "exploredNodes": len(agent.explored), "timeTaken": endTime}
    agent.reset()

    # Return the results
    return response
