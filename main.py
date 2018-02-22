import pygame
from pygame.locals import *
from math import *
from Hexagone import Hexagone
from tkinter import *
from Grid import Grid


def main():
    pygame.init()
    width, height = 1200, 750

    display = pygame.display.set_mode((width, height))

    white = (255, 255, 255)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)

    bg = pygame.image.load("src\img\Map3_clean_reduced.png")
    myfont = pygame.font.SysFont("monospace", 15)
    display.blit(bg, (0, 0))

    barbare = pygame.image.load("src/img/barbare.png")

    hexagone_start = Hexagone(0, 0)
    myGrid = Grid(5, 10, display, white, red, barbare, hexagone_start)

    for h in myGrid.hexagones:
        h.draw(display, white)
        if h.selected:
            h.draw(display, red)
            display.blit(barbare, (h.q - 17 / 2, h.r - 25 / 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                display.blit(bg, (0, 0))

                for hex in myGrid.hexagones:
                    d = sqrt((mouse_x - hex.q) ** 2 + (mouse_y - hex.r) ** 2)
                    if d < hex.size:
                        myGrid.move(hex)
                        print(str(hex.row) + ':' + str(hex.col))
                        terrain = myGrid.terrain[hex.row][hex.col]
                        print(terrain.name)
                        print("\n")
                        break
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


main()
