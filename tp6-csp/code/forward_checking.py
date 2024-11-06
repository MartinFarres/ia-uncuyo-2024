import matplotlib.pyplot as plt
from matplotlib import colors


class NQueensForwardCheckingSolver:
    def __init__(self, n):
        self.n = n
        self.solution = None
        # Inicializamos todos los dominios
        self.domains = {i: set(range(n)) for i in range(n)}
        self.states_explored = 0
        # Conjuntos para rastrear columnas y diagonales ocupadas
        self.columns = set()
        self.diagonals1 = set()  # r - c
        self.diagonals2 = set()  # r + c

    def is_safe(self, row, col):
        # Verificar si la posición está ocupada
        return col not in self.columns and (row - col) not in self.diagonals1 and (row + col) not in self.diagonals2

    def forward_check(self, row, col):
        # Marcar la columna y diagonales como ocupadas
        self.columns.add(col)
        self.diagonals1.add(row - col)
        self.diagonals2.add(row + col)

        # Actualizar dominios de las filas siguientes
        for i in range(row + 1, self.n):
            self.domains[i].discard(col)
            self.domains[i].discard(i - row + col)
            self.domains[i].discard(i + row - col)

    def undo_forward_check(self, row, col):
        # Restaurar columnas y diagonales ocupadas
        self.columns.remove(col)
        self.diagonals1.remove(row - col)
        self.diagonals2.remove(row + col)

        # Restaurar los dominios afectados en filas inferiores
        for i in range(row + 1, self.n):
            self.domains[i].add(col)
            self.domains[i].add(i - row + col)
            self.domains[i].add(i + row - col)

    def solve(self, board, row):
        if row == self.n:
            self.solution = list(board)
            return True

        # Selección de la columna de menor dominio en la fila actual
        for col in sorted(self.domains[row], key=lambda c: len(self.domains.get(row, set()))):
            if self.is_safe(row, col):
                self.states_explored += 1
                board[row] = col
                original_domains = {k: set(v) for k, v in self.domains.items()}
                self.forward_check(row, col)

                if self.solve(board, row + 1):
                    return True

                # Restauramos el dominio tras el backtracking
                self.domains = original_domains
                self.undo_forward_check(row, col)

        return False

    def run(self):
        board = [-1] * self.n
        self.solve(board, 0)
        return self.solution, 0, self.states_explored

    def plot(self, board):
        chessboard = [[0 if (i + j) % 2 == 0 else 1 for j in range(self.n)]
                      for i in range(self.n)]
        queens = [(row, col) for row, col in enumerate(board)]

        fig, ax = plt.subplots()
        cm = colors.ListedColormap(["white", "black"])

        for row, col in queens:
            color = "white" if chessboard[row][col] == 1 else "black"
            ax.text(col, row, "♛", ha="center",
                    va="center", color=color, fontsize=20)

        ax.set_xticks([])
        ax.set_yticks([])
        ax.imshow(chessboard, cmap=cm)
        plt.show()
