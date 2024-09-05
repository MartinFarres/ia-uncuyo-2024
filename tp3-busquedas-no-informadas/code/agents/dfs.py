from typing import Tuple
from collections import deque
from agent import Agent
from map import Map

class DfsAgent(Agent):
    def __init__(self, maxDepth: int = 10000):
        super().__init__()
        self.maxDepth = maxDepth

    def searchAlgorithm(self, map: Map):
        depth = 0
        self.frontier: deque[Tuple[int, int]] = deque([map.startPos])  # Initialize with agent start pos
        self.maxDepth 
        while len(self.frontier) > 0 and self.lives > 0:
            nodeToExamine = self.frontier.pop()  # Efficient pop from the left
            
            self.explored.add(nodeToExamine)
            for action_idx, action in enumerate(self.actionsFunctions):
                nodeChild = action(map, nodeToExamine)
                
                if nodeChild:
                    if nodeChild not in self.explored and nodeChild not in self.frontier:
                        depth += 1
                        if depth > self.maxDepth:
                          continue
                        self.actionDict[nodeChild] = (action_idx, nodeToExamine)
                        if nodeChild == map.goalPos:
                            self.setActionsList(map)
                            return
                        self.frontier.append(nodeChild)  # Efficient append to the right
                else: 
                    depth -= 1
            
            self.lives -= 1
        self.setActionsList(map)
        