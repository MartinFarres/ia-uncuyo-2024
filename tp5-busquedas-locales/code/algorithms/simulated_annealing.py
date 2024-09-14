import math
import time
from environment import pairQueensInCheck
from random import randint, random

# Nunca baja de 1-2    ¯\_ (ツ)_/¯


def simulatedAnnealing(env, maxStates=10000, initialTemp=100, coolingRate=0.95) -> list[int]:
    bestValue = env.value
    bestEnv = env.env

    currentValue = bestValue
    currentEnv = bestEnv.copy()

    startTime = time.time()

    for states in range(maxStates):
        if currentValue == 0:
            return env

        # Calculate time and get T
        elapsedTime = time.time() - startTime
        T = schedule(elapsedTime, initialTemp, coolingRate)

        if T <= 0:
            return env

        # Get successors
        successors = []
        for i in range(env.size):
            posToCheck = [x for x in range(env.size) if x != currentEnv[i]]
            for pos in posToCheck:
                successorEnv = currentEnv.copy()
                successorEnv[i] = pos
                successorValue = pairQueensInCheck(env.size, successorEnv)
                successors.append((successorEnv, successorValue))

        # Randomly select a successor
        nextEnv, nextValue = successors[randint(0, len(successors) - 1)]
        deltaE = nextValue - currentValue

        if deltaE < 0:  # is < because we look for a global minima
            currentValue, currentEnv = nextValue, nextEnv
        else:
            # Accept the worse state with probability exp(-ΔE / T)
            probability = math.exp(-deltaE / T)
            if random() < probability:
                currentValue, currentEnv = nextValue, nextEnv

        # Update the best solution found
        if currentValue < bestValue:
            bestValue, bestEnv = currentValue, currentEnv.copy()

    env.env, env.value = bestEnv, bestValue
    return env


def schedule(elapsedTime, initialTemp, coolingRate):
    return initialTemp * (coolingRate ** (elapsedTime / 1000))
