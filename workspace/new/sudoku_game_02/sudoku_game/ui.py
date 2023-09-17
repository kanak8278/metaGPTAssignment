from typing import Tuple

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
