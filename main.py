import pygame
from math import *

from Game import Game
from Hexagone import Hexagone
from tkinter import *
from Grid import Grid
from Player import Player


def main():
    pygame.init()
    width, height = 1200, 750
    display = pygame.display.set_mode((width, height))

    white, blue, red, green = (255, 255, 255), (0, 0, 255), (255, 0, 0), (0, 255, 0)
    row, col = 15, 20
    round_end = 5
    player = Player()
    player_start = Hexagone(0, 0)

    board = Grid(row, col, display, white, red, player, player_start)
    game = Game(board, player, round_end)

    game.grid.init()

    while True:
        #if game.end():
        #    print("The End")
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                game.grid.clear()
                for hex in board.hexagones:
                    d = sqrt((mouse_x - hex.q) ** 2 + (mouse_y - hex.r) ** 2)
                    if d < hex.size:
                        player.move(game, hex)

                        game.end_turn()
                        """
                        print(str(hex.row) + ':' + str(hex.col))
                        terrain = myGrid.terrain[hex.row][hex.col]
                        print(terrain.name)
                        print("\n")
                        break
                        """
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


main()
