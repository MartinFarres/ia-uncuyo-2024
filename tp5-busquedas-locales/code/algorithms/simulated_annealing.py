import math
import time
from environment import pairQueensInCheck, Environment
from random import randint, random


def simulatedAnnealing(env: Environment, initialTemp=100000, coolingRate=0.1, minTemp=0.01) -> Environment:
    bestValue = env.value
    bestEnv = env.env

    currentValue = bestValue
    currentEnv = bestEnv.copy()
    T = initialTemp
    startTime = time.time()

    states = 0

    while T > minTemp:
        states += 1
        if currentValue == 0:
            return env

        # Calculate time and get T
        elapsedTime = time.time() - startTime
        T = schedule(T, coolingRate, elapsedTime)
        print(T)
        if T <= 0:
            return env

        # Randomly select a successor
        nextEnv = currentEnv.copy()
        while nextEnv == currentEnv:
            nextEnv[randint(0, len(nextEnv) - 1)
                    ] = randint(0, (len(nextEnv) - 1))

        nextValue = pairQueensInCheck(env.size, nextEnv)
        deltaE = nextValue - currentValue

        # Update the best solution found
        if nextValue < bestValue:
            bestValue, bestEnv = nextValue, nextEnv.copy()

        # Accept the worse state with probability exp(-ΔE / T)
        if deltaE > 0 or random() < math.exp(-deltaE / T):
            currentValue, currentEnv = nextValue, nextEnv

    env.env, env.value, env.states_explored = bestEnv, bestValue, states
    return env


def schedule(temp, coolingRate, elapsedTime):
    return temp / (1 + coolingRate * math.log(1 + elapsedTime))
