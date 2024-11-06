import matplotlib.pyplot as plt
from matplotlib import colors


class NQueensBacktrackingSolver:
    def __init__(self, n):
        self.n = n
        self.solution = None
        self.states_explored = 0
        # Conjuntos para rastrear columnas y diagonales ocupadas
        self.columns = set()
        self.diagonals1 = set()  # r - c (diagonal principal)
        self.diagonals2 = set()  # r + c (diagonal secundaria)

    def is_safe(self, row, col):
        # Verificar si la columna o diagonales están ocupadas
        return col not in self.columns and (row - col) not in self.diagonals1 and (row + col) not in self.diagonals2

    def place_queen(self, row, col):
        # Agregar la reina en la posición dada
        self.columns.add(col)
        self.diagonals1.add(row - col)
        self.diagonals2.add(row + col)

    def remove_queen(self, row, col):
        # Eliminar la reina de la posición dada
        self.columns.remove(col)
        self.diagonals1.remove(row - col)
        self.diagonals2.remove(row + col)

    def solve(self, board, row):
        if row == self.n:
            self.solution = list(board)
            return True
        for col in range(self.n):
            if self.is_safe(row, col):
                self.states_explored += 1  # Contar cada estado seguro explorado
                board[row] = col
                self.place_queen(row, col)

                if self.solve(board, row + 1):
                    return True

                # Backtracking: eliminar la reina y deshacer cambios
                self.remove_queen(row, col)
        return False

    def run(self):
        board = [-1] * self.n
        self.solve(board, 0)
        # 0 conflictos porque no se calculan explícitamente
        return self.solution, 0, self.states_explored
