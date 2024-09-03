from typing import List, Optional, Tuple
import gymnasium as gym
from gymnasium.utils import seeding

# IMPORTANT: POSITIONS=[Y,X]

class Map:
  def __init__(self, size:int, p:float, isSlippery: Optional[bool]=False, seed:Optional[int]= None) -> None:
    self.size = size
    self.p = p
    self.seed = seed
    self.startPos: Tuple[int,int]
    self.goalPos: Tuple[int,int]
    self.startPos, self.goalPos = self.generateRandomPositions()
    self.desc = self.generateMap()
    self.env = gym.make("FrozenLake-v1",desc=self.desc, is_slippery=isSlippery, render_mode="human")

  def generateRandomPositions(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        np_random, _ = seeding.np_random(self.seed) 
        startPos = (np_random.integers(0, self.size), np_random.integers(0, self.size))
        goalPos = startPos
        while goalPos == startPos: # Ensures goalPos != startPos
            goalPos = (np_random.integers(0, self.size), np_random.integers(0, self.size))
        return startPos, goalPos
  
  def generateMap(self)->List[str]:
    board = [] # Initialize board

    # Set np_random with seed
    np_random, _ = seeding.np_random(self.seed) 

    # Creates Desc
    self.p = min(1, self.p)
    board = np_random.choice(["F", "H"], (self.size, self.size), p=[self.p, 1 - self.p]) 
    
    # Set random start pos & goal pos
    board[self.startPos[0]][self.startPos[1]] = "S"
    board[self.goalPos[0]][self.goalPos[1]] = "G"

    print(["".join(x) for x in board])
    return ["".join(x) for x in board]
  
  
 