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
    round_end = 70
    player = Player()

    grid = Grid(row, col, display, white, red, player)
    game = Game(grid, player, round_end)

    game.grid.init()

    while game.end():
        game.draw_chat()
        game.game_launch(False)

        rDay = Rect(875, 650, 150, 75)
        pygame.draw.rect(display, black, rDay, 3)
        labelDay = grid.font.render("Semaine : "+str(int(game.current_round/7)+1), 1, black)
        labelDay2 = grid.font.render("Jour : "+str(game.current_round), 1, black)
        display.blit(labelDay, (rDay.left + rDay.width * 1 / 7, rDay.top + rDay.height * 1 / 10))
        display.blit(labelDay2, (rDay.left + rDay.width * 1 / 7, rDay.top + rDay.height * 1 / 10 + 25))

        rPlayer = Rect(1050, 650, 150, 75)
        pygame.draw.rect(display, black, rPlayer, 3)
        labelGold = grid.font.render("Argent : "+str(player.gold), 1, black)
        labelHealth = grid.font.render("PV : "+str(player.health), 1, black)
        display.blit(labelGold, (rPlayer.left + rPlayer.width * 1 / 7, rPlayer.top + rPlayer.height * 1 / 10))
        display.blit(labelHealth, (rPlayer.left + rPlayer.width * 1 / 7, rPlayer.top + rPlayer.height * 1 / 10 + 25))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                game.grid.clear()
                if game.status == "Not playing":
                    game.start(mouse_x, mouse_y)
                else:
                    inGrid = False
                    for hex in game.grid.hexagones:
                        d = sqrt((mouse_x - hex.q) ** 2 + (mouse_y - hex.r) ** 2)
                        if d < hex.size:
                            inGrid = True
                            player.move(game, hex, game.test_move(hex))
                            break
                    if not inGrid:
                        for hex in game.grid.hexagones:
                            if hex.selected:
                                game.grid.draw_player(hex)
                                break

            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


main()
