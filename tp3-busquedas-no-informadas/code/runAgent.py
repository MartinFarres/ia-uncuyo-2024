from map import Map
from agents.agent import Agent
import time
import sys
sys.path.append('./agents')

# Recommendation: Comment Print & UI sections for bulk runs


def runAgent(map: Map, agent: Agent):
    # Env Definitions & Clean state
    map.generateNewMap()

    agent.reset()
    # nuevoLimite = 1000
    # env = wrappers.TimeLimit(map.env, nuevoLimite)
    env = map.env
    state = env.reset()

    # Get Time
    startTime = time.time()
    agent.searchAlgorithm(map)
    endTime = time.time() - startTime

    # # Print
    # print(map.desc)
    # if len(agent.actionsList) > 0:
    #     response = {"totalCost": agent.calculateCost(),
    #                 "exploredNodes": len(agent.explored), "timeTaken": endTime}
    # else:
    #     print("Goal not achieved")

    # UI
    # actions = agent.actionsList
    # done = truncated = False
    # while not (done or truncated):
    #     try:
    #         action = actions.pop()
    #     except Exception as err:  # Catch all exceptions
    #         break
    #     next_state, reward, done, truncated, info = env.step(action)
    #     state = next_state
    # env.close()

    # Return the results
    response = {"costE1": agent.calculateCost(), "costE2": agent.calculateCost(True),
                "exploredNodes": len(agent.explored), "timeTaken": endTime,
                "solutionFound": len(agent.actionsList) > 0, "envSeed": map.seed}
    return response
