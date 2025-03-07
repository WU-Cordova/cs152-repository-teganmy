from __future__ import annotations
import random
from datastructures.array2d import Array2D
from projects.project2.cell import Cell

class Grid:
    def __init__(self, rows: int=10, cols:int=10):
        self.grid: Array2D[Cell] = Array2D.empty(rows, cols, data_type = Cell)
        self.rows = rows
        self.cols = cols
        for row in range(rows):
            for col in range(cols):
                self.grid[row][col] = Cell(random.choice([True, False]))

    def display(self) -> None:
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.grid[row][col], end = "")
            print()
        print()

    def get_neighbors(self, row, col) -> int:
        neighbors = 0

        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if (r - 1 > 0) and (r + 1 <= self.rows) and (c - 1 > 0) and (c + 1 <= self.cols):
                    if not (r == row and c == col):
                        if self.grid[r][c].is_alive:
                                neighbors += 1
        return neighbors

    def next_generation(self) -> Grid:
        next_grid = Grid(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                num_neighbors = self.get_neighbors(row, col)
                next_state = self.grid[row][col].next_state(num_neighbors)
                next_grid.grid[row][col].is_alive = next_state
        return next_grid

    def __eq__(self, value):
        if isinstance(value, Grid) and self.rows == value.rows and self.cols == value.cols:
            return self.grid == value.grid
        return False
