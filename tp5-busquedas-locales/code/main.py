from environment import Environment
from algorithms.hill_climbing import hillClimbing
from algorithms.simulated_annealing import simulatedAnnealing

env = Environment(9)
print(env.env)
print(env.value)
env = simulatedAnnealing(env)
print(env.env)
print(env.value)
