from environment import Environment
from algorithms.hill_climbing import hillClimbing

env = Environment(4)
print(env.env)
print(env.value)
env = hillClimbing(env)
print(env.env)
print(env.value)
