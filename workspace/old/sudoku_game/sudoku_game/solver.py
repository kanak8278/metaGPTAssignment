## solver.py
from typing import Tuple
from grid import Grid

class Solver:
    def solve(self, grid: Grid) -> bool:
        """
        Solve the Sudoku puzzle using backtracking.

        Args:
            grid (Grid): The Sudoku grid to solve.

        Returns:
            bool: True if the puzzle is solvable, False otherwise.
        """
        # Find the next empty cell
        row, col = self.find_empty_cell(grid)

        # If there are no empty cells, the puzzle is solved
        if row == -1 and col == -1:
            return True

        # Try different values for the empty cell
        for value in range(1, 10):
            if grid.is_valid_move(row, col, value):
                # Set the value in the grid
                grid.set_cell(row, col, value)

                # Recursively solve the puzzle
                if self.solve(grid):
                    return True

                # If the puzzle cannot be solved with the current value, backtrack
                grid.set_cell(row, col, 0)

        return False

    def find_empty_cell(self, grid: Grid) -> Tuple[int, int]:
        """
        Find the next empty cell in the grid.

        Args:
            grid (Grid): The Sudoku grid.

        Returns:
            Tuple[int, int]: The row and column indices of the empty cell, or (-1, -1) if no empty cell is found.
        """
        for row in range(9):
            for col in range(9):
                if grid.get_cell(row, col) == 0:
                    return row, col
        return -1, -1
