## ui.py
import pygame
import pygame_gui

class UI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.manager = pygame_gui.UIManager((800, 600))
        self.clock = pygame.time.Clock()

    def draw_grid(self, grid):
        """
        Draw the Sudoku grid on the screen.
        
        Args:
            grid (Grid): The Sudoku grid to draw.
        """
        # TODO: Implement drawing the grid
        pass

    def draw_cell(self, row, col, value):
        """
        Draw a cell on the grid with the given value.
        
        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
            value (int): The value of the cell.
        """
        # TODO: Implement drawing a cell
        pass

    def highlight_cell(self, row, col):
        """
        Highlight a cell on the grid.
        
        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
        """
        # TODO: Implement highlighting a cell
        pass

    def get_input(self):
        """
        Get user input for making a move.
        
        Returns:
            Tuple[int, int, int]: The row, column, and value of the move.
        """
        # TODO: Implement getting user input
        pass

    def show_message(self, message):
        """
        Show a message on the screen.
        
        Args:
            message (str): The message to show.
        """
        # TODO: Implement showing a message
        pass
