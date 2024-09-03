from map import Map
from gymnasium import wrappers
from bfs import BfsAgent

map = Map(50, 0.8)
nuevoLimite = 100
env = wrappers.TimeLimit(map.env, nuevoLimite)

state = env.reset()
agent = BfsAgent(map)
print(agent.actionsList)
done = truncated = False
while not (done or truncated):
  action = agent.actionsList.pop(0)
  next_state, reward, done, truncated, _ = env.step(action)
  state = next_state
