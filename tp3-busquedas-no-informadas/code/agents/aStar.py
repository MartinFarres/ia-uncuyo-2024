from typing import Tuple
from queue import PriorityQueue
from agent import Agent
from map import Map


class AStarAgent(Agent):
    def __init__(self, costByAction: bool = False, costByManhattan: bool = True):
        super().__init__(costByAction=costByAction)
        self.costByManhattan = costByManhattan

    def searchAlgorithm(self, map: Map):
        frontier: PriorityQueue[Tuple[int, Tuple[int, int]]] = PriorityQueue()
        frontierSet = set()
        priorityDict = dict()
        # Initialize with agent start pos
        frontierSet.add(map.startPos)
        frontier.put((0, map.startPos))
        priorityDict[map.startPos] = self.calculatePriority(
            map.startPos, map.goalPos, 0)

        while not frontier.empty():
            nodePriority, nodeToExamine = frontier.get()
            frontierSet.discard(nodeToExamine)
            self.explored.add(nodeToExamine)

            for action_idx, action in enumerate(self.actionsFunctions):
                nodeChild = action(map, nodeToExamine)

                if len(nodeChild) == 0:
                    continue

                # Calculate ChildPriority
                childPriority = nodePriority + \
                    self.calculatePriority(nodeChild, map.goalPos, action_idx)

                if nodeChild not in self.explored and nodeChild not in frontierSet:
                    # Set to action dictionary the action and node parent
                    self.actionDict[nodeChild] = (action_idx, nodeToExamine)

                    if nodeChild == map.goalPos:
                        self.setActionsList(map)
                        return

                    # Efficient append to the right
                    frontier.put((childPriority, nodeChild))
                    frontierSet.add(nodeChild)
                    priorityDict[nodeChild] = childPriority
                else:
                    if priorityDict[nodeChild] > childPriority:
                        # Set to action dictionary the action and node parent
                        self.actionDict[nodeChild] = (
                            action_idx, nodeToExamine)
                        priorityDict[nodeChild] = childPriority
                        frontier.put((childPriority, nodeChild))

    def calculatePriority(self, node, goal, action_idx):
        distToGoal = abs(node[0] - goal[0]) + abs(node[1] - goal[1])
        if self.costByManhattan:
            return distToGoal
        else:
            return distToGoal + action_idx
