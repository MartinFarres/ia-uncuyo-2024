from environment import Environment
import random


class Agent:
  def __init__(self, env: Environment): 
    self.position = [env.initPosX, env.initPosY]
    self.env = env
  
  def up(self):
    if self.position[1] == 0:
      # raise IndexError("Out of bounds")
      return
    self.position = [self.position[0], self.position[1] - 1]
  
  def down(self):
    if self.position[1] == self.env.sizeY-1:
      # raise IndexError("Out of bounds")
      return
    self.position = [self.position[0], self.position[1] + 1]

  def left(self):
    if self.position[0] == 0:
      # raise IndexError("Out of bounds")
      return
    self.position = [self.position[0] - 1, self.position[1]]
  
  def right(self):
    if self.position[0] == self.env.sizeX-1:
      # raise IndexError("Out of bounds")
      return
    self.position = [self.position[0] + 1, self.position[1]]
  
  def idle(self):
    pass

  def suck(self):
    cell = self.env.getCell(self.position)
    if not cell.isDirty:
        return
    cell.clean()
    self.env.cleanCells += 1
    self.env.dirtyCells -= 1


class RandomAgent(Agent):
  def think(self):
    actions = []
    actions.append(self.down)
    actions.append(self.up)
    actions.append(self.right)
    actions.append(self.left)
    actions.append(self.idle)
    actions.append(self.suck)

    actions[random.randrange(0, len(actions))]()

    

class ReflexiveSimpleAgent(Agent):
  def perspective(self):
    cell = self.env.getCell(self.position)
    return cell.isDirty

  def think(self):
    if self.perspective():
      self.suck()
      return
    actions = []

    if self.position[1] <= self.env.sizeY - 1:
        actions.append(self.down)

    if self.position[1] > 0:
        actions.append(self.up)

    if self.position[0] <= self.env.sizeX - 1:
        actions.append(self.right)

    if self.position[0] > 0:
        actions.append(self.left)

    actions[random.randrange(0, len(actions))]()
   

