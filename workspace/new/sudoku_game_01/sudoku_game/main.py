"""
main.py
Main entry point of the game
"""

import pygame
import pygame_gui
import pygame_menu
import pygame_text

from game import Game
from menu import Menu

# Initialize pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Sudoku Game")

# Set up the game clock
clock = pygame.time.Clock()

# Set up the game manager
game = Game(window_width, window_height)
menu = Menu(window_width, window_height)

# Set up the game menu
main_menu = pygame_menu.Menu(window_height, window_width, "Sudoku Game", theme=pygame_menu.themes.THEME_DARK)
main_menu.add_button("Start Game", game.start_new_game)
main_menu.add_selector("Difficulty", [("Easy", "easy"), ("Medium", "medium"), ("Hard", "hard")], onchange=game.change_difficulty)
main_menu.add_button("Quit", pygame_menu.events.EXIT)

# Set up the game GUI manager
gui_manager = pygame_gui.UIManager((window_width, window_height))

# Set up the game text renderer
text_renderer = pygame_text.TextRenderer()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Pass events to the game manager
        game.handle_event(event)

        # Pass events to the menu
        menu.handle_event(event)

        # Pass events to the GUI manager
        gui_manager.process_events(event)

    # Update the game
    game.update()

    # Update the menu
    menu.update()

    # Clear the window
    window.fill((255, 255, 255))

    # Render the game
    game.render(window)

    # Render the menu
    menu.render(window)

    # Render the GUI
    gui_manager.draw_ui(window)

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Clean up pygame
pygame.quit()
