"""
grid.py
Contains the Grid class for managing the sudoku grid
"""

from typing import List

from cell import Cell

class Grid:
    def __init__(self):
        self.cells = []

    def get_cell(self, row: int, col: int) -> Cell:
        """
        Get the cell at the specified row and column.
        """
        return self.cells[row][col]

    def is_valid_move(self, row: int, col: int, number: int) -> bool:
        """
        Check if the specified move is valid in the grid.
        """
        cell = self.get_cell(row, col)
        if not cell.is_editable():
            return False

        # Check if the number already exists in the row
        for i in range(9):
            if self.get_cell(row, i).get_value() == number:
                return False

        # Check if the number already exists in the column
        for i in range(9):
            if self.get_cell(i, col).get_value() == number:
                return False

        # Check if the number already exists in the 3x3 box
        box_row = row // 3
        box_col = col // 3
        for i in range(box_row * 3, box_row * 3 + 3):
            for j in range(box_col * 3, box_col * 3 + 3):
                if self.get_cell(i, j).get_value() == number:
                    return False

        return True

    def is_complete(self) -> bool:
        """
        Check if the grid is complete.
        """
        for row in self.cells:
            for cell in row:
                if cell.get_value() == 0:
                    return False

        return True
