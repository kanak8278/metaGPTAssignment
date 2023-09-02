## grid.py

from typing import List, Optional, Tuple

class Grid:
    def __init__(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]

    def set_cell_value(self, row: int, col: int, value: int) -> None:
        """
        Set the value of a cell in the grid.
        
        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
            value (int): The value to set in the cell.
        """
        self.grid[row][col] = value

    def get_cell_value(self, row: int, col: int) -> int:
        """
        Get the value of a cell in the grid.
        
        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
        
        Returns:
            int: The value of the cell.
        """
        return self.grid[row][col]

    def is_valid_move(self, row: int, col: int, value: int) -> bool:
        """
        Check if a move is valid.
        
        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
            value (int): The value to check.
        
        Returns:
            bool: True if the move is valid, False otherwise.
        """
        # Check row
        for i in range(9):
            if self.grid[row][i] == value:
                return False
        
        # Check column
        for i in range(9):
            if self.grid[i][col] == value:
                return False
        
        # Check 3x3 box
        box_row = row // 3 * 3
        box_col = col // 3 * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.grid[i][j] == value:
                    return False
        
        return True

    def is_complete(self) -> bool:
        """
        Check if the grid is complete.
        
        Returns:
            bool: True if the grid is complete, False otherwise.
        """
        for row in self.grid:
            if 0 in row:
                return False
        return True
