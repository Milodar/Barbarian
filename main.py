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

    hexagones = []
    myGrid = Grid()

    for row in range(20):
        for col in range(20):
            hex = Hexagone(row, col)
            hex.oddq_to_cube()
            hex.cube_to_axial()
            p = hex.hex_to_pixel()
            hex.q = p.x + 64
            hex.r = p.y + 90

            #label = myfont.render(str(hex.row) + "." + str(hex.col), 1, (255, 0, 0))
            #display.blit(label, (hex.q, hex.r))

            hexagones.append(hex)
            hex.draw(display, white)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                display.blit(bg, (0, 0))

                for hex in hexagones:
                    d = sqrt((mouse_x - hex.q) ** 2 + (mouse_y - hex.r) ** 2)
                    if d < hex.size:
                        for h in hexagones:
                            h.draw(display, white)
                            if h.selected:
                                h.selected = False
                        hex.selected = True
                        #lstNeighbours = hex.neighbours()

                        hex.draw(display, red)

                        display.blit(barbare, (hex.q - 17/2, hex.r - 25/2))
                        break
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


main()
