from typing import List, Optional, Tuple
import gymnasium as gym
from gymnasium.utils import seeding

# IMPORTANT: POSITIONS=[Y,X]


class Map:
    def __init__(self, size: int, p: float, isSlippery: Optional[bool] = False, seed: Optional[int] = None, render=False) -> None:
        self.size = size
        self.p = p
        self.np_random, self.seed = seeding.np_random(seed)
        self.startPos: Tuple[int, int]
        self.goalPos: Tuple[int, int]
        self.generateRandomPositions()
        self.desc = [[]]
        self.generateMap()
        self.isSlippery = isSlippery
        self.render = "human" if render else None
        self.env = gym.make("FrozenLake-v1", desc=self.desc,
                            is_slippery=isSlippery, render_mode=self.render)

    def generateRandomPositions(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:

        startPos = (self.np_random.integers(0, self.size),
                    self.np_random.integers(0, self.size))
        goalPos = startPos
        while goalPos == startPos:  # Ensures goalPos != startPos
            goalPos = (self.np_random.integers(0, self.size),
                       self.np_random.integers(0, self.size))
        self.startPos, self.goalPos = startPos, goalPos
        return

    def generateMap(self):
        board = []  # Initialize board

        # Set np_random with seed

        # Creates Desc
        self.p = min(1, self.p)
        board = self.np_random.choice(
            ["F", "H"], (self.size, self.size), p=[self.p, 1 - self.p])

        # Set random start pos & goal pos
        board[self.startPos[0]][self.startPos[1]] = "S"
        board[self.goalPos[0]][self.goalPos[1]] = "G"

        self.desc = ["".join(x) for x in board]

        return

    def generateNewMap(self):
        self.generateRandomPositions()
        self.generateMap()
        self.env = gym.make("FrozenLake-v1", desc=self.desc,
                            is_slippery=self.isSlippery, render_mode=self.render)
        return
