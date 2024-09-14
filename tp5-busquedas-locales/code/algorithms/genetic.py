from environment import Environment
from random import randint, random


def geneticAlgorithm(popSize: int = 100, envSize: int = 8, maxGenerations=100) -> Environment:
    # Generates Population
    currentPop = generatePop(popSize, envSize)

    # Iterates through generations
    for generation in range(maxGenerations):
        newPop = []

        # Elitism: Keep the best individual from the current population
        bestIndividual = min(currentPop, key=lambda env: env.value)
        newPop.append(bestIndividual)

        # Iterates through the Current Population to get a Better Generation
        for i in range(popSize - 1):  # -1 because of elitism
            # Get Parents
            xIndividual = randomSelection(currentPop, envSize)
            yIndividual = randomSelection(currentPop, envSize)

            # Reproduce
            child = reproduce(xIndividual, yIndividual)

            # Mutation with 5% probability
            if random() < 0.05:
                child.env[randint(0, envSize-1)] = randint(0, envSize-1)
                child.updateValue()

            # Check for global minima
            if child.value == 0:
                print(f"Global minima found in generation {generation}")
                return child

            newPop.append(child)

        # Advances Population
        currentPop = newPop

    # Return the best individual found
    return min(currentPop, key=lambda env: env.value)


def reproduce(xIndividual: Environment, yIndividual: Environment) -> Environment:
    # Random crossover point
    c = randint(0, xIndividual.size - 1)

    # Combine xIndividual's env up to index c and yIndividual's env after index c
    childEnv = xIndividual.env[:c] + yIndividual.env[c:]

    # Return the new Environment with the combined env
    return Environment(xIndividual.size, childEnv)


def randomSelection(currentPop: list[Environment], envSize) -> Environment:
    # Max value of non attacking pairs / when h = 0
    maxValue = envSize*(envSize-1) / 2

    # Calculate sum of values
    totalValue = sum(maxValue - env.value for env in currentPop)

    # Creates hash table with accumulative percentages
    cumulativeTable = {}
    cumulative = 0
    for env in currentPop:
        percentage = (maxValue - env.value) / totalValue * 100
        cumulative += percentage
        cumulativeTable[cumulative] = env

    # Get env with random number
    rand = random() * 100
    for cumulativeLimit in sorted(cumulativeTable.keys()):
        if rand <= cumulativeLimit:
            return cumulativeTable[cumulativeLimit]


def generatePop(popSize, envSize) -> list[Environment]:
    return [Environment(envSize) for _ in range(popSize)]
