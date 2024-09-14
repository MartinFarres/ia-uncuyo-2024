from environment import Environment
from algorithms.hill_climbing import hillClimbing
from algorithms.simulated_annealing import simulatedAnnealing
from algorithms.genetic import geneticAlgorithm


env = geneticAlgorithm()
print(env.env)
print(env.value)
