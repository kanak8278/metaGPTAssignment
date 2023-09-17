from typing import Tuple

class SudokuGrid:
    def __init__(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]

    def get_cell(self, row: int, col: int) -> int:
        return self.grid[row][col]

    def set_cell(self, row: int, col: int, number: int) -> None:
        self.grid[row][col] = number

    def is_valid_move(self, row: int, col: int, number: int) -> bool:
        for i in range(9):
            if self.grid[row][i] == number or self.grid[i][col] == number:
                return False

        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.grid[box_row + i][box_col + j] == number:
                    return False

        return True

    def is_complete(self) -> bool:
        for row in self.grid:
            if 0 in row:
                return False
        return True

class SudokuUI:
    def __init__(self, grid: SudokuGrid):
        self.grid = grid

    def draw(self) -> None:
        # TODO: Implement drawing logic for the Sudoku grid
        pass

    def handle_input(self) -> None:
        # TODO: Implement input handling logic for the Sudoku grid
        pass

    def show_hint(self, row: int, col: int, number: int) -> None:
        # TODO: Implement logic to show a hint to the player
        pass

    def show_progress(self, correct_cells: int) -> None:
        # TODO: Implement logic to show the player's progress
        pass
