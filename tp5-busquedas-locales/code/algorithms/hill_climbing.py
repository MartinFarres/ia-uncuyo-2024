from environment import pairQueensInCheck


def hillClimbing(env, maxStates=1000) -> list[int]:
    currentValue = env.value
    currentEnv = env.env

    for states in range(maxStates):
        # Get Succesors
        for i in range(env.size):
            posToCheck = [x for x in range(env.size) if x != currentEnv[i]]

            # Check successors for each possible move
            for pos in posToCheck:
                # Copy of the current environment to modify for this successor
                childEnv = currentEnv.copy()
                childEnv[i] = pos
                childValue = pairQueensInCheck(env.size, childEnv)

                if childValue < currentValue:
                    currentValue, currentEnv = childValue, childEnv

                    if childValue == 0:
                        env.env, env.value = currentEnv, currentValue
                        return env

        env.env, env.value, env.states_explored = currentEnv, currentValue, states
    return env
