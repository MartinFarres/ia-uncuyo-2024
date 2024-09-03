from typing import Tuple
from collections import deque
from agent import Agent
from map import Map

class DfsAgent(Agent):
    def __init__(self, map: Map, maxDepth: int = None):
        super().__init__()
        self.explored = set()
        self.frontier: deque[Tuple[int, int]] = deque([map.startPos])  # Initialize with agent start pos
        self.maxDepth = maxDepth
        self.dfsFunction(map)
        self.setActionsList(map)

    def dfsFunction(self, map: Map):
        depth = 0
        while self.frontier:
            nodeToExamine = self.frontier.pop()  # Efficient pop from the left
            
            self.explored.add(nodeToExamine)
            for action_idx, action in enumerate(self.actionsFunctions):
                nodeChild = action(map, nodeToExamine)
                
                if nodeChild:
                    if nodeChild not in self.explored and nodeChild not in self.frontier:
                        depth += 1
                        if depth > self.maxDepth:
                          continue
                        print(depth)
                        self.actionDict[nodeChild] = (action_idx, nodeToExamine)
                        if nodeChild == map.goalPos:
                            break
                        self.frontier.append(nodeChild)  # Efficient append to the right
                else: 
                  depth -= 1
