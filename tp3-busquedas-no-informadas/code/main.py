from map import Map
from gymnasium import wrappers
from bfs import BfsAgent
from dfs import DfsAgent

map = Map(5, 0.8, seed=12664)
nuevoLimite = 100
env = wrappers.TimeLimit(map.env, nuevoLimite)

state = env.reset()
agent = DfsAgent(map, maxDepth=10)
print(agent.actionsList)
done = truncated = False
while not (done or truncated):
  action = agent.actionsList.pop(0)
  next_state, reward, done, truncated, _ = env.step(action)
  state = next_state
