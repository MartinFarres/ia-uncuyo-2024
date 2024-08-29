from environment import Environment
from agents import Agent

def iteration(env:Environment, agent:Agent):
  i = 0
  while (True):
    # if (i % 1000 == 0) or (i ==0):
    #   env.printEnvironment(agent.position)

    if env.dirtyCells == 0:
      # print(f"Iterations: {i} \n Cleaned Cells: {env.cleanCells} \n")
      # env.printEnvironment(agent.position)
      break
    
    agent.think()
    

    i += 1
  
  return i


# if __name__ == "__main__":
  





  


