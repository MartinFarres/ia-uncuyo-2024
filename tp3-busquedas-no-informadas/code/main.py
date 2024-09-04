import time
from map import Map
from gymnasium import wrappers
from agent import Agent
from plot import generateBoxPlot

# Recommendation: Comment Print & UI sections for bulk runs 
def runAgent(map:Map, agent:Agent)->object:
  # Env Definitions & Clean sleet
  map.generateMap() # Generates new random map
  nuevoLimite = 100
  env = wrappers.TimeLimit(map.env, nuevoLimite)
  state = env.reset()
  
  # Get Time
  startTime = time.time()
  agent.searchAlgorithm(map)
  endTime = time.time() - startTime
  
  # Print
  # print(map.desc)
  # if(len(agent.actionsList)) > 0:
  #   print("Action List: ", agent.actionsList)
  #   print("Explored Node: ", len(agent.explored))
  #   print("Time Taken: ", endTime)
  # else:
  #   print("Goal not achived")

  # UI
  # done = truncated = False
  # while not (done or truncated):
  #   try:
  #     action = agent.actionsList.pop(0)
  #   except Exception as err:  # Catch all exceptions
  #     raise Exception(f"An error occurred: {err}")
  #   next_state, done, truncated, _ = env.step(action)
  #   state = next_state
  # env.close()


  return {"totalCost": len(agent.actionsList), "totalCostByAction": agent.calculateCost(True),
           "exploredNodes": agent.explored, "timeTaken": endTime}



# Generates Plots
if __name__ == "__main__":
  generateBoxPlot()