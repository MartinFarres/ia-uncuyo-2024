from random import randint


class Environment:
    def __init__(self, size) -> None:
        self.size = size
        self.env = [randint(0, size-1) for _ in range(size)]
        self.value = pairQueensInCheck(self.size, self.env)


def pairQueensInCheck(size=None, env=None) -> int:
    pairs = set()

    for i in range(size):
        for j in range(i + 1, size):
            # Si están en la misma fila
            if env[i] == env[j]:
                pairs.add((i, j))

            # Si están en la misma diagonal
            if abs(env[i] - env[j]) == abs(i - j):
                pairs.add((i, j))
    return len(pairs)
