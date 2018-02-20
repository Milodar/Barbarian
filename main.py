import pygame, sys
from pygame.locals import *
from math import *
from Point import *
from Hexagone import Hexagone


def main():

    pygame.init()
    display = pygame.display.set_mode((1280, 720), RESIZABLE)

    white = (255, 255, 255)
    blue = (0, 0, 255)

    #bg = pygame.image.load("BarbarianPrince_map2.jpg")
    #display.blit(bg, (0, 0))
    display.fill(white)

    Hexagones = []

    myfont = pygame.font.SysFont("monospace", 15)

    w, h = pygame.display.get_surface().get_size()
    for row in range(-3, 3):
        for col in range(-3, 3):
            hex = Hexagone(row, col)
            hex.oddr_to_cube()
            hex.cube_to_axial()
            p = hex.hex_to_pixel()
            hex.q = p.x + (w/2)
            hex.r = p.y + (h/2)

            label = myfont.render(str(hex.row) + "." + str(hex.col), 1, (255, 0, 0))
            display.blit(label, (hex.q, hex.r))

            Hexagones.append(hex)
            hex.draw(display, blue)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print(" CLICK ")
                print(mouse_x)
                print(mouse_y)

                hex1 = Hexagone(0,0)
                hex1.pixel_to_hex(mouse_x, mouse_y)
                print("Hexagone : [" + str(hex1.q) + " | " + str(hex1.r) + "]")
            elif event.type == pygame.MOUSEBUTTONUP:
                print(" CLICK UP")
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


main()