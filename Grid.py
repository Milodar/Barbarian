import pygame

from Terrain import Terrain as t
from Hexagone import Hexagone


class Grid:
    def __init__(self, row_grid, col_grid, screen, clear_color, player_color, player):
        self.terrain = [
            [t(1), t(6), t(6), t(4), t(4), t(1), t(1), t(3), t(6), t(3), t(3), t(4), t(1), t(5), t(2), t(2), t(3), t(6), t(6), t(6)],
            [t(1), t(4), t(4), t(4), t(1), t(1), t(1), t(4), t(1), t(4), t(3), t(4), t(5), t(1), t(5), t(1), t(3), t(6), t(6), t(6)],
            [t(6), t(4), t(4), t(6), t(6), t(6), t(6), t(4), t(4), t(3), t(5), t(3), t(1), t(1), t(4), t(6), t(6), t(1), t(6), t(3)],
            [t(1), t(3), t(6), t(6), t(6), t(1), t(1), t(6), t(3), t(1), t(1), t(6), t(4), t(4), t(4), t(4), t(1), t(6), t(3), t(1)],
            [t(3), t(3), t(1), t(6), t(4), t(3), t(4), t(4), t(1), t(1), t(6), t(1), t(1), t(3), t(6), t(6), t(6), t(6), t(1), t(3)],
            [t(7), t(7), t(7), t(3), t(3), t(4), t(1), t(3), t(1), t(6), t(6), t(6), t(3), t(3), t(6), t(7), t(6), t(6), t(1), t(6)],
            [t(3), t(3), t(3), t(7), t(1), t(1), t(1), t(4), t(1), t(4), t(3), t(6), t(6), t(7), t(7), t(7), t(7), t(6), t(6), t(3)],
            [t(1), t(1), t(1), t(4), t(4), t(1), t(1), t(4), t(4), t(1), t(3), t(3), t(7), t(7), t(7), t(7), t(7), t(3), t(6), t(6)],
            [t(1), t(1), t(4), t(4), t(4), t(5), t(4), t(4), t(1), t(2), t(3), t(3), t(7), t(7), t(7), t(7), t(3), t(6), t(6), t(3)],
            [t(1), t(1), t(4), t(1), t(1), t(4), t(5), t(1), t(1), t(3), t(1), t(1), t(3), t(3), t(7), t(3), t(7), t(6), t(6), t(3)],
            [t(4), t(1), t(1), t(5), t(5), t(5), t(4), t(4), t(4), t(3), t(6), t(6), t(6), t(3), t(3), t(6), t(3), t(3), t(1), t(6)],
            [t(1), t(1), t(5), t(1), t(1), t(1), t(4), t(4), t(3), t(1), t(3), t(6), t(4), t(3), t(3), t(3), t(6), t(3), t(3), t(6)],
            [t(1), t(5), t(5), t(1), t(4), t(1), t(5), t(4), t(4), t(1), t(3), t(1), t(6), t(4), t(1), t(1), t(3), t(3), t(3), t(3)],
            [t(5), t(5), t(4), t(4), t(4), t(1), t(1), t(4), t(5), t(1), t(6), t(6), t(1), t(2), t(1), t(1), t(1), t(1), t(1), t(1)],
            [t(5), t(4), t(4), t(1), t(1), t(1), t(4), t(4), t(4), t(5), t(1), t(3), t(1), t(2), t(2), t(1), t(4), t(4), t(1), t(4)],
            [t(4), t(1), t(1), t(1), t(4), t(1), t(4), t(1), t(2), t(1), t(1), t(1), t(2), t(1), t(1), t(1), t(4), t(1), t(4), t(1)]
        ]
        self.hexagones = []
        self.display = screen
        self.bg = pygame.image.load("src\img\Map3_clean_reduced.png")
        self.clear_color = clear_color
        self.player_color = player_color
        self.player_token = player.token
        self.font = pygame.font.SysFont("Trebuchet MS", 15)
        for row in range(row_grid):
            for col in range(col_grid):
                hex = Hexagone(col, row)
                hex.oddq_to_cube()
                hex.cube_to_axial()
                p = hex.hex_to_pixel()
                hex.q = p.x + 64
                hex.r = p.y + 90
                self.hexagones.append(hex)

    def init(self):
        self.display.blit(self.bg, (0, 0))
        self.clear()
        for h in self.hexagones:
            if h.selected:
                self.draw_player(h)
                break

    def clear(self):
        self.display.blit(self.bg, (0, 0))
        for h in self.hexagones:
            h.draw(self.display, self.clear_color)

    def draw_player(self, hex):
        hex.draw(self.display, self.player_color)
        self.display.blit(self.player_token, (hex.q - 17 / 2, hex.r - 25 / 2))

    def draw_dice(self, img, pos):
        self.display.blit(img, (pos.left + pos.width * 1 / 3, pos.top + pos.height * 2 / 3))