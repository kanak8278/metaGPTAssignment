## solver.py
from typing import List

class Solver:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid

    def solve(self) -> bool:
        """
        Solve the sudoku grid.
        """
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            return True

        row, col = empty_cell

        for num in range(1, 10):
            if self.is_valid_move(row, col, num):
                self.grid[row][col] = num

                if self.solve():
                    return True

                self.grid[row][col] = 0

        return False

    def find_empty_cell(self) -> tuple[int, int]:
        """
        Find the next empty cell in the grid.
        """
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    return row, col

        return None

    def is_valid_move(self, row: int, col: int, num: int) -> bool:
        """
        Check if the specified move is valid in the grid.
        """
        # Check if the number already exists in the row
        for i in range(9):
            if self.grid[row][i] == num:
                return False

        # Check if the number already exists in the column
        for i in range(9):
            if self.grid[i][col] == num:
                return False

        # Check if the number already exists in the 3x3 box
        box_row = row // 3
        box_col = col // 3
        for i in range(box_row * 3, box_row * 3 + 3):
            for j in range(box_col * 3, box_col * 3 + 3):
                if self.grid[i][j] == num:
                    return False

        return True
