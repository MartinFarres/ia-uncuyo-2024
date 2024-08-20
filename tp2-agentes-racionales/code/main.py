from environment import Environment
from agents import RandomAgent, ReflexiveSimpleAgent


if __name__ == "__main__":
  i = 0
  dirtRate = 0.3

  env = Environment(5,5,0,0,dirtRate)

  agent = ReflexiveSimpleAgent(env)

  while (i <= 1000):
    if (i % 10 == 0) or (i ==0):
      env.printEnvironment(agent.position)

    if env.dirtyCells == 0:
      print(f"Iterations: {i} \n Cleaned Cells: {env.cleanCells} \n")
      env.printEnvironment(agent.position)
      break
    
    agent.think()
    

    i += 1





  


