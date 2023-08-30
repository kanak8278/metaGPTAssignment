## game.py
from typing import Tuple
from grid import Grid
from ui import UI
from puzzles import Puzzles
from solver import Solver

class Game:
    def __init__(self):
        self.grid = Grid()
        self.ui = UI()
        self.puzzles = Puzzles()
        self.solver = Solver()

    def start_new_game(self, difficulty: str) -> None:
        """
        Start a new game with the specified difficulty level.

        Args:
            difficulty (str): The difficulty level of the game (easy, medium, hard).
        """
        self.grid = self.puzzles.generate_puzzle(difficulty)
        self.ui.draw_grid(self.grid)

    def check_solution(self) -> bool:
        """
        Check if the current solution is correct.

        Returns:
            bool: True if the solution is correct, False otherwise.
        """
        return self.solver.solve(self.grid)

    def get_hint(self) -> Tuple[int, int, int]:
        """
        Get a hint for the current game.

        Returns:
            Tuple[int, int, int]: The row, column, and value of the hint cell.
        """
        row, col = self.solver.find_empty_cell(self.grid)
        value = self.grid.get_cell(row, col)
        return row, col, value

    def save_game(self, file_path: str) -> None:
        """
        Save the current game progress to a file.

        Args:
            file_path (str): The file path to save the game progress.
        """
        with open(file_path, "w") as file:
            for row in self.grid:
                file.write(" ".join(str(cell) for cell in row) + "\n")

    def load_game(self, file_path: str) -> None:
        """
        Load the game progress from a file.

        Args:
            file_path (str): The file path to load the game progress from.
        """
        with open(file_path, "r") as file:
            lines = file.readlines()
            self.grid = [[int(cell) for cell in line.strip().split()] for line in lines]
        self.ui.draw_grid(self.grid)
