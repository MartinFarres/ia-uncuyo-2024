from typing import Optional, Tuple
from queue import PriorityQueue
from agent import Agent
from map import Map

class UcsAgent(Agent):
    def __init__(self, costByAction:bool = False):
        super().__init__(costByAction=costByAction)
        
        
    def searchAlgorithm(self, map: Map):
        frontier: PriorityQueue[Tuple[int, Tuple[int, int]]] = PriorityQueue()
        frontierSet = set()
        frontier.put((0,map.startPos))  # Initialize with agent start pos
        frontierSet.add(map.startPos)
        while not frontier.empty() :
            nodePriority, nodeToExamine = frontier.get()  
            frontierSet.remove(nodeToExamine)
            self.explored.add(nodeToExamine)

            for action_idx, action in enumerate(self.actionsFunctions):
                nodeChild = action(map, nodeToExamine)

                if nodeChild:
                    if nodeChild not in self.explored and nodeChild not in frontierSet:
                        self.actionDict[nodeChild] = (action_idx, nodeToExamine)

                        if nodeChild == map.goalPos:
                            self.setActionsList(map)
                            return
                        
                        frontier.put((nodePriority + action_idx, nodeChild))  # Efficient append to the right
                        frontierSet.add(nodeChild)

    

