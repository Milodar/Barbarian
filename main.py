import pygame, sys
from pygame.locals import *
from math import *
from Point import *
from Hexagone import Hexagone
from tkinter import *

def main():
    pygame.init()
    width, height = 1920, 1080

    display = pygame.display.set_mode((width, height), RESIZABLE)

    white = (255, 255, 255)
    blue = (0, 0, 255)
    red = (255, 0, 0)

    bg = pygame.image.load("src\img\Map3_clean_reduced.png")
    #bg = pygame.transform.scale(bg, (width, height))
    display.blit(bg, (0, 0))
    #display.fill(white)

    Hexagones = []

    myfont = pygame.font.SysFont("monospace", 15)

    w, h = pygame.display.get_surface().get_size()
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

            Hexagones.append(hex)
            hex.draw(display, white)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                for hex in Hexagones:
                    d = sqrt( (mouse_x - hex.q)**2 + (mouse_y - hex.r)**2 )
                    if d < hex.size:
                        for h in Hexagones:
                            if h.selected:
                                h.selected = False
                                h.draw(display, white)
                        hex.selected = True
                        hex.draw(display, red)
                        break
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


main()
