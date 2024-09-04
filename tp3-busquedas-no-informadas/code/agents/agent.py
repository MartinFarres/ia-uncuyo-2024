from abc import abstractmethod
from typing import Dict, Tuple
from map import Map

class Agent:
  def __init__(self, lives:int = 99999, costByAction:bool = False ):
    self.actionDict:Dict[Tuple[int,int], Tuple[int,Tuple[int,int]]] = dict()
    self.actionsFunctions = [self.moveLeft, self.moveDown, self.moveRight, self.moveUp]
    self.actionsList = []
    self.lives = lives
    self.explored = set()
    self.costByAction = costByAction

  @abstractmethod
  def searchAlgorithm(self, map: Map):
    ...

  def setActionsList(self, map: Map):
    # If goal not achieved
    if map.goalPos not in self.actionDict:
      return
    
    pos = map.goalPos
    
    # Goal achieved
    while pos != map.startPos:  # Init position
        movementValue = self.actionDict[pos]  # Action to get here & Parent Pos
        action = movementValue[0]
        self.actionsList.append(action)

        # Get the position of the parent node
        parentPos = movementValue[1]

        # Move to the parent position
        pos = parentPos
        
        
    # Reverse the actions list to get the correct order from start to goal
    self.actionsList.reverse()

    


  def calculateCost(self):
    # When each action costs 1
    if not self.costByAction:
      return len(self.actionsList)
    
    # When each action costs 1 + action index
    return len(self.actionsList) + sum(self.actionsList)
  
  
  def moveUp(self, map: Map, startPos: Tuple[int, int]) -> Tuple[int, int]:
    if startPos[0] > 0:
        newPos = (startPos[0]-1, startPos[1])
        if map.desc[newPos[0]][newPos[1]] != "H":
            return newPos
    return ()

  def moveDown(self, map: Map, startPos: Tuple[int, int]) -> Tuple[int, int]:
    if startPos[0] < (map.size - 1):
        newPos = (startPos[0]+1, startPos[1])
        if map.desc[newPos[0]][newPos[1]] != "H":
            return newPos
    return ()

  def moveLeft(self, map: Map, startPos: Tuple[int, int]) -> Tuple[int, int]:
    if startPos[1] > 0:
        newPos = (startPos[0], startPos[1]-1)
        if map.desc[newPos[0]][newPos[1]] != "H":
            return newPos
    return ()

  def moveRight(self, map: Map, startPos: Tuple[int, int]) -> Tuple[int, int]:
    if startPos[1] < (map.size - 1):
        newPos = (startPos[0] , startPos[1]+1)
        if map.desc[newPos[0]][newPos[1]] != "H":
            return newPos
    return ()
