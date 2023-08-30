"""
import pygame
from typing import Tuple
from grid import Grid

class UI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.font = pygame.font.Font(None, 36)

    def draw_grid(self, grid: Grid) -> None:
        self.screen.fill((255, 255, 255))
        for row in range(9):
            for col in range(9):
                value = grid.get_cell(row, col)
                editable = value == 0
                self.draw_cell(row, col, value, editable)
        pygame.display.flip()

    def draw_cell(self, row: int, col: int, value: int, editable: bool) -> None:
        x = col * 60
        y = row * 60
        pygame.draw.rect(self.screen, (0, 0, 0), (x, y, 60, 60), 1)
        if value != 0:
            text = self.font.render(str(value), True, (0, 0, 0))
            text_rect = text.get_rect(center=(x + 30, y + 30))
            self.screen.blit(text, text_rect)
        if editable:
            pygame.draw.rect(self.screen, (255, 0, 0), (x + 1, y + 1, 58, 58), 1)

    def get_user_input(self) -> Tuple[int, int, int]:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return -1, -1, -1
                    elif event.key == pygame.K_1:
                        return pygame.K_1, -1, -1
                    elif event.key == pygame.K_2:
                        return pygame.K_2, -1, -1
                    elif event.key == pygame.K_3:
                        return pygame.K_3, -1, -1
                    elif event.key == pygame.K_4:
                        return pygame.K_4, -1, -1
                    elif event.key == pygame.K_5:
                        return pygame.K_5, -1, -1
                    elif event.key == pygame.K_6:
                        return pygame.K_6, -1, -1
                    elif event.key == pygame.K_7:
                        return pygame.K_7, -1, -1
                    elif event.key == pygame.K_8:
                        return pygame.K_8, -1, -1
                    elif event.key == pygame.K_9:
                        return pygame.K_9, -1, -1
                    elif event.key == pygame.K_BACKSPACE:
                        return pygame.K_BACKSPACE, -1, -1
                    elif event.key == pygame.K_LEFT:
                        return -1, pygame.K_LEFT, -1
                    elif event.key == pygame.K_RIGHT:
                        return -1, pygame.K_RIGHT, -1
                    elif event.key == pygame.K_UP:
                        return -1, -1, pygame.K_UP
                    elif event.key == pygame.K_DOWN:
                        return -1, -1, pygame.K_DOWN

    def display_message(self, message: str) -> None:
        text = self.font.render(message, True, (0, 0, 0))
        text_rect = text.get_rect(center=(300, 550))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
"""
