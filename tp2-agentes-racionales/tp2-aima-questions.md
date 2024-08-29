# Responder las preguntas 2.10 y 2.11 de AIMA 3ra Edicion.

## 2.10 Consider a modified version of the vacuum environment in Exercise 2.8, in which the agent is penalized one point for each movement.

### a. Can a simple reflex agent be perfectly rational for this environment? Explain.

No, an agent would not be rational if it is penalized one point for each movement, as it would move infinitely, whether it encounters dirt or not, and would be penalized all the time. Therefore, it would not be rational, as it would not maximize the performance measure. This is because it has no memory of the dirty squares it has passed through, and it also does not know the environment in advance.

### b. What about a reflex agent with state? Design such an agent.

If it stored information about its current state and the dirty squares it passed through, it still wouldn’t know the environment in its entirety, so it wouldn’t be rational.

### c. How do your answers to a and b change if the agent’s percepts give it the clean/dirty status of every square in the environment?

In this case, the agent would be rational since it would know the state of each square and would only make moves when necessary (when a square is dirty).

## 2.11 Consider a modified version of the vacuum environment in Exercise 2.8, in which the geography of the environment—its extent, boundaries, and obstacles—is unknown, as is the initial dirt configuration. (The agent can go Up and Down as well as Left and Right.)

### a. Can a simple reflex agent be perfectly rational for this environment? Explain.

A simple reflex agent would not be rational in this environment because it has no “memory”; it cannot estimate what it does not perceive, and it makes decisions based solely on its immediate perception. Additionally, it would have no prior knowledge of the environment (extent, boundaries, etc.), which could result in a highly inefficient path, leaving areas of the environment unexplored, for example.

### b. Can a simple reflex agent with a randomized agent function outperform a simple reflex agent? Design such an agent and measure its performance on several environments.

As can be seen from the results obtained in Exercises 4 and 5, a randomized agent does not perform better than a simple reflex agent.

### c. Can you design an environment in which your randomized agent will perform poorly? Show your results.

A randomized agent would likely perform poorly in an environment where the probability of a square being dirty is low, but also in a very large environment due to the low probability of the agent passing over a dirty square.

### d. Can a reflex agent with state outperform a simple reflex agent? Design such an agent and measure its performance on several environments. Can you design a rational agent of this type?

Yes, a reflex agent with state can outperform a simple reflex agent because a state-based agent has the ability to remember what it has done and where it has been, allowing it to make more informed decisions and avoid retracing the same path.
