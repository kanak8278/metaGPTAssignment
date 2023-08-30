## puzzles.py

from typing import List
from sudoku import Sudoku

class Puzzles:
    @staticmethod
    def generate_puzzle(difficulty: str) -> List[List[int]]:
        """
        Generate a Sudoku puzzle of the specified difficulty level.

        Args:
            difficulty (str): The difficulty level of the puzzle (easy, medium, hard).

        Returns:
            List[List[int]]: The generated Sudoku puzzle as a 2D list of integers.
        """
        puzzle = Sudoku(difficulty=difficulty)
        puzzle.generate()
        return puzzle.board
