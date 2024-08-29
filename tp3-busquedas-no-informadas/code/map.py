from typing import List, Optional, Tuple
import gymnasium as gym
from gymnasium.utils import seeding

class Map:
  def __init__(self, size:int, p:float, isSlippery: Optional[bool]=False, seed:Optional[int]= None) -> None:
    self.size = size
    self.p = p
    self.seed = seed
    desc = self.generateMap()
    self.env = gym.make("FrozenLake-v1",desc=desc, is_slippery=isSlippery, render_mode="human")

  def generateMap(self)->List[str]:
    board = [] # Initialize board

    # Set np_random with seed
    np_random, _ = seeding.np_random(self.seed) 

    # Creates Desc
    self.p = min(1, self.p)
    board = np_random.choice(["F", "H"], (self.size, self.size), p=[self.p, 1 - self.p]) 
    
    # Set random start pos & goal pos
    startPos, goalPos = self.generateRandomPositions(np_random)
    board[startPos[0]][startPos[1]] = "S"
    board[goalPos[0]][goalPos[1]] = "G"

    return ["".join(x) for x in board]
  
  def generateRandomPositions(self, np_random) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        startPos = (np_random.integers(0, self.size), np_random.integers(0, self.size))
        goalPos = startPos
        while goalPos == startPos: # Ensures goalPos != startPos
            goalPos = (np_random.integers(0, self.size), np_random.integers(0, self.size))
        return startPos, goalPos
  
 