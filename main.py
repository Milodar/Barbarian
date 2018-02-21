import pygame
from pygame.locals import *
from math import *
from Hexagone import Hexagone
from tkinter import *


def main():
    pygame.init()
    width, height = 1200, 750

    display = pygame.display.set_mode((width, height), RESIZABLE)

    white = (255, 255, 255)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)

    bg = pygame.image.load("src\img\Map3_clean_reduced.png")
    display.blit(bg, (0, 0))

    hexagones = []

    myfont = pygame.font.SysFont("monospace", 15)

    #w, h = pygame.display.get_surface().get_size()
    for row in range(-10, 10):
        for col in range(-11, 12):
            hex = Hexagone(row, col)
            hex.oddq_to_cube()
            hex.cube_to_axial()
            p = hex.hex_to_pixel()
            hex.q = p.x + 448.5
            hex.r = p.y + 580

            #label = myfont.render(str(hex.row) + "." + str(hex.col), 1, (255, 0, 0))
            #display.blit(label, (hex.q, hex.r))

            hexagones.append(hex)
            hex.draw(display, white)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                for hex in hexagones:
                    d = sqrt((mouse_x - hex.q) ** 2 + (mouse_y - hex.r) ** 2)
                    if d < hex.size:
                        for h in hexagones:
                            h.draw(display, white)
                            if h.selected:
                                h.selected = False
                        hex.selected = True
                        lstNeighbours = hex.neighbours()
                        for neighbour in lstNeighbours:
                            for h in hexagones:
                                if neighbour.col == h.col and neighbour.row == h.row:
                                    h.draw(display, green)
                        hex.draw(display, red)
                        break
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


main()
