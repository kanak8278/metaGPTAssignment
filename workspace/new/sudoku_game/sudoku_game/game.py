"""
game.py
Contains the Game class for managing the game logic
"""

import pygame
import pygame_gui
import pygame_menu
import pygame_text

from grid import Grid
from solver import Solver
from menu import Menu
from text import Text

class Game:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.score = 0
        self.time = 0
        self.grid = Grid()
        self.solver = Solver()
        self.menu = Menu()
        self.text = Text()

    def start_new_game(self, difficulty):
        """
        Start a new game with the specified difficulty level.
        """
        self.score = 0
        self.time = 0
        self.grid.create(difficulty)

    def input_number(self, row, col, number):
        """
        Input a number in the game grid at the specified row and column.
        """
        cell = self.grid.get_cell(row, col)
        if cell.is_editable():
            cell.set_value(number)

    def check_solution(self):
        """
        Check if the game grid is solved correctly.
        """
        return self.grid.is_complete() and self.solver.solve(self.grid)

    def get_hint(self):
        """
        Get a hint for the next move.
        """
        hint_row, hint_col, hint_number = self.solver.get_hint(self.grid)
        return hint_row, hint_col, hint_number

    def change_difficulty(self, difficulty):
        """
        Change the difficulty level of the game.
        """
        self.grid.create(difficulty)

    def handle_event(self, event):
        """
        Handle events for the game.
        """
        # Handle events for the menu
        self.menu.handle_event(event)

        # Handle events for the grid
        self.grid.handle_event(event)

    def update(self):
        """
        Update the game state.
        """
        # Update the menu
        self.menu.update()

        # Update the grid
        self.grid.update()

    def render(self, window):
        """
        Render the game elements to the window.
        """
        # Render the menu
        self.menu.render(window)

        # Render the grid
        self.grid.render(window)

        # Render the text
        self.text.render(window)
