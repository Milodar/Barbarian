import pygame
from math import *

from pygame.rect import Rect

from Game import Game
from Hexagone import Hexagone
from tkinter import *
from Grid import Grid
from Player import Player

from random import randint




def main():
    pygame.init()
    width, height = 1200, 750
    display = pygame.display.set_mode((width, height))

    white, blue, red, green, black = (255, 255, 255), (0, 0, 255), (255, 0, 0), (0, 255, 0), (0, 0, 0)
    row, col = 15, 20
    round_end = 5
    player = Player()

    grid = Grid(row, col, display, white, red, player)
    game = Game(grid, player, round_end)

    game.grid.init()

    while game.end():
        game.draw_chat()
        game.game_launch()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                game.grid.clear()
                if game.status == "Playing":
                    for hex in game.grid.hexagones:
                        d = sqrt((mouse_x - hex.q) ** 2 + (mouse_y - hex.r) ** 2)
                        if d < hex.size:
                            player.move(game, hex, game.test_move(hex))
                            #game.end_turn()
                            break
                else:
                    game.start(mouse_x, mouse_y)
                    game.status = "Beginning"


            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


main()
