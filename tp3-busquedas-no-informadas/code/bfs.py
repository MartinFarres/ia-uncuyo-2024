from typing import Tuple
from collections import deque
from agent import Agent
from map import Map

class BfsAgent(Agent):
    def __init__(self, map: Map):
        super().__init__()
        self.explored = set()
        self.frontier: deque[Tuple[int, int]] = deque([map.startPos])  # Initialize with agent start pos
        self.bfsFunction(map)
        self.setActionsList(map)
    def bfsFunction(self, map: Map):
        while self.frontier:
            nodeToExamine = self.frontier.popleft()  # Efficient pop from the left
            
            self.explored.add(nodeToExamine)
            for action_idx, action in enumerate(self.actionsFunctions):
                nodeChild = action(map, nodeToExamine)
                
                if nodeChild:
                    if nodeChild not in self.explored and nodeChild not in self.frontier:
                        self.actionDict[nodeChild] = (action_idx, nodeToExamine)
                        if nodeChild == map.goalPos:
                            break
                        self.frontier.append(nodeChild)  # Efficient append to the right

