from typing import Tuple
from collections import deque
from agent import Agent
from map import Map


class BfsAgent(Agent):
    def __init__(self):
        super().__init__()

    def searchAlgorithm(self, map: Map):
        frontier: deque[Tuple[int, int]] = deque(
            [map.startPos])  # Initialize with agent start pos

        while len(frontier) > 0:
            nodeToExamine = frontier.popleft()  # Efficient pop from the left

            self.explored.add(nodeToExamine)
            for action_idx, action in enumerate(self.actionsFunctions):
                nodeChild = action(map, nodeToExamine)

                if nodeChild:
                    if nodeChild not in self.explored and nodeChild not in frontier:
                        self.actionDict[nodeChild] = (
                            action_idx, nodeToExamine)
                        if nodeChild == map.goalPos:
                            self.setActionsList(map)
                            return
                        # Efficient append to the right
                        frontier.append(nodeChild)
