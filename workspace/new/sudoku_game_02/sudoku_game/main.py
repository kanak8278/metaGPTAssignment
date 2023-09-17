import pygame
from sudoku import SudokuGame
from ui import SudokuUI

def main():
    pygame.init()
    game = SudokuGame()
    ui = SudokuUI(game.grid)

    game.start_new_game("easy")
    ui.draw()

    while True:
        ui.handle_input()

if __name__ == "__main__":
    main()
