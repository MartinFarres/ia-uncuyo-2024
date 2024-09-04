import time
from map import Map
from gymnasium import wrappers
from agent import Agent

def main(map:Map, agent:Agent):
  # Env Definitions & Clean sleet
  nuevoLimite = 100
  env = wrappers.TimeLimit(map.env, nuevoLimite)
  state = env.reset()
  
  # Get Time
  startTime = time.time()
  agent.searchAlgorithm(map)
  endTime = time.time() - startTime

  # Print
  if(len(agent.actionsList)) > 0:
    print("Action List: ", agent.actionsList)
    print("Explored Node: ", len(agent.explored))
    print("Time Taken: ", endTime)
  else:
    print("Goal not achived")

  # UI
  done = truncated = False
  while not (done or truncated):
    try:
      action = agent.actionsList.pop(0)
    except Exception as err:  # Catch all exceptions
      raise Exception(f"An error occurred: {err}")
    next_state, done, truncated, _ = env.step(action)
    state = next_state
