import random


class Cell:
  def __init__(self, dirtRate ):
    self.isDirty = True if random.random() <= dirtRate else False
  def clean(self):
      self.isDirty = False
    

class Environment:
  def __init__(self, sizeX, sizeY, initPosX, initPosY, dirtRate):
    self.room = [[Cell(dirtRate) for i in range(sizeX)] for j in range(sizeY)]
    self.sizeX = sizeX
    self.sizeY = sizeY
    self.initPosX = initPosX
    self.initPosY = initPosY
    self.dirtyCells = 0
    self.cleanCells = 0

    self.countCellState()
  
  def getCell(self, pos)->Cell:
      x, y = pos
      return self.room[x][y]

  def countCellState(self):
        for row in self.room:
            for cell in row:
                if cell.isDirty:
                    self.dirtyCells += 1      
  

  def printEnvironment(self, agentPos):
        print(agentPos)
        for y, row in enumerate(self.room):
            rowStr = "| "
            for x, cell in enumerate(row):
                if cell.isDirty and [x,y] == agentPos:
                    marker = "RD"  
                elif cell.isDirty:
                    marker = "D"
                elif [x,y] == agentPos:
                    marker = "R"
                else:
                    marker = "_"  
                rowStr += marker + " | "
            print(rowStr)
        print()
