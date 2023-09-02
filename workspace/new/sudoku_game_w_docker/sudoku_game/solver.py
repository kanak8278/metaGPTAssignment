## solver.py
from grid import Grid

class Solver:
    def solve(self, grid: Grid) -> bool:
        """
        Solve a Sudoku puzzle.
        
        Args:
            grid (Grid): The Sudoku grid to solve.
        
        Returns:
            bool: True if the puzzle is solvable, False otherwise.
        """
        # Find an empty cell
        row, col = grid.get_empty_cell()
        
        # If there are no empty cells, the puzzle is solved
        if row is None or col is None:
            return True
        
        # Try each possible value for the empty cell
        for value in range(1, 10):
            # Check if the move is valid
            if grid.is_valid_move(row, col, value):
                # Set the value in the grid
                grid.set_cell_value(row, col, value)
                
                # Recursively solve the puzzle
                if self.solve(grid):
                    return True
                
                # If the puzzle cannot be solved with this value, backtrack
                grid.set_cell_value(row, col, 0)
        
        # If no value leads to a solution, the puzzle is unsolvable
        return False
