from typing import Dict, Tuple
from map import Map

class Agent:
  def __init__(self):
    self.actionDict:Dict[Tuple[int,int], Tuple[int,Tuple[int,int]]] = dict()
    self.actionsFunctions = [self.moveLeft, self.moveDown, self.moveRight, self.moveUp]
    self.actionsList = []

  def setActionsList(self, map: Map):
    # If goal not achieved
    if map.goalPos not in self.actionDict:
        print("Goal position not found in actionDict.")
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

    


  def calculateCost(self, byAction=False):
    # When each action costs 1
    if not byAction:
        return len(self.actionsList)
    
    # When each action costs 1 + action index
    return sum([1 + action for action in self.actionsList])
  
  
  def moveUp(self, map: Map, startPos: Tuple[int, int]) -> Tuple[int, int]:
    if startPos[0] > 0:
        newPos = (startPos[0]-1, startPos[1])
        if map.desc[newPos[0]][newPos[1]] != "H":
            # print(map.desc[newPos[0]][newPos[1]])
            return newPos
    return ()

  def moveDown(self, map: Map, startPos: Tuple[int, int]) -> Tuple[int, int]:
    if startPos[0] < (map.size - 1):
        newPos = (startPos[0]+1, startPos[1])
        if map.desc[newPos[0]][newPos[1]] != "H":
            # print(map.desc[newPos[0]][newPos[1]])
            return newPos
    return ()

  def moveLeft(self, map: Map, startPos: Tuple[int, int]) -> Tuple[int, int]:
    if startPos[1] > 0:
        newPos = (startPos[0], startPos[1]-1)
        if map.desc[newPos[0]][newPos[1]] != "H":
            # print(map.desc[newPos[0]][newPos[1]])
            return newPos
    return ()

  def moveRight(self, map: Map, startPos: Tuple[int, int]) -> Tuple[int, int]:
    if startPos[1] < (map.size - 1):
        newPos = (startPos[0] , startPos[1]+1)
        if map.desc[newPos[0]][newPos[1]] != "H":
            # print(map.desc[newPos[0]][newPos[1]])
            return newPos
    return ()
