from typing import Tuple, Deque, Set, Dict
from collections import deque
from agent import Agent
from map import Map

class DfsAgent(Agent):
    def __init__(self, maxDepth: int = 10000):
        super().__init__()
        self.maxDepth = maxDepth

    def searchAlgorithm(self, map: Map):
        """Algoritmo de búsqueda en profundidad con límite de profundidad y evitación de revisitas."""
        # Inicializar la frontera con el nodo inicial
        frontier: Deque[Tuple[int, int]] = deque([(map.startPos, 0)])  # Nodo inicial y profundidad
        frontierAux: Set[Tuple[int, int]] = {map.startPos}  # Conjunto auxiliar para evitar duplicados
        parentDict: Dict[Tuple[int, int], Tuple[int, int]] = {map.startPos: None}  # Diccionario de padres
        self.explored: Set[Tuple[int, int]] = set()  # Nodos completamente explorados

        while frontier:
            nodeToExamine, currentDepth = frontier.pop()  # Obtener el último nodo de la frontera (DFS)
            frontierAux.discard(nodeToExamine)  # Eliminar de la frontera auxiliar

            if nodeToExamine in self.explored:
                continue  # Saltar nodos ya explorados
            
            self.explored.add(nodeToExamine)  # Marcar el nodo como explorado

            # Si hemos alcanzado la meta, construimos la lista de acciones y terminamos
            if nodeToExamine == map.goalPos:
                self.setActionsList(map)
                return

            # Procesar nodos hijos si la profundidad es menor que el máximo permitido
            if currentDepth < self.maxDepth:
                for action_idx, action in enumerate(self.actionsFunctions):
                    nodeChild = action(map, nodeToExamine)

                    # Si el nodo hijo es válido, no ha sido explorado ni está en la frontera
                    if nodeChild and nodeChild not in self.explored and nodeChild not in frontierAux:
                        parentDict[nodeChild] = nodeToExamine  # Guardar el nodo padre
                        self.actionDict[nodeChild] = (action_idx, nodeToExamine)  # Registrar la acción y el padre
                        frontier.append((nodeChild, currentDepth + 1))  # Añadir el nodo hijo a la frontera con profundidad incrementada
                        frontierAux.add(nodeChild)  # Añadir el nodo hijo al conjunto auxiliar
