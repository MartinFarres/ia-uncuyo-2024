from typing import Optional, Tuple
from queue import PriorityQueue
from agent import Agent
from map import Map

class UcsAgent(Agent):
    def __init__(self, map: Map, costByAction:bool = False):
        super().__init__(costByAction=costByAction)
        self.frontier: PriorityQueue[Tuple[int, Tuple[int, int]]] = PriorityQueue()
        self.frontierSet = set()
        self.frontier.put((0,map.startPos))  # Initialize with agent start pos
        self.frontierSet.add(map.startPos)
        
    def searchAlgorithm(self, map: Map):
        while not self.frontier.empty() and self.lives > 0:
            nodePriority, nodeToExamine = self.frontier.get()  
            self.frontierSet.remove(nodeToExamine)
            self.explored.add(nodeToExamine)

            for action_idx, action in enumerate(self.actionsFunctions):
                nodeChild = action(map, nodeToExamine)

                if nodeChild:
                    if nodeChild not in self.explored and nodeChild not in self.frontierSet:
                        self.actionDict[nodeChild] = (action_idx, nodeToExamine)

                        if nodeChild == map.goalPos:
                            break
                        
                        self.frontier.put((nodePriority + action_idx, nodeChild))  # Efficient append to the right
                        self.frontierSet.add(nodeChild)

            self.lives -= 1
        self.setActionsList(map)
        self.frontier.empty()
        self.frontierSet.clear()
        
