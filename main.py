import pygame
from pygame.locals import *
from math import *
from Hexagone import Hexagone
from tkinter import *
from Grid import Grid
from random import randint


def launchdice(nbdice):
    dice = []
    for i in range(nbdice):
        die = randint(1, 6)
        dice.append(die)
    return dice


def main():
    pygame.init()
    width, height = 1200, 750

    display = pygame.display.set_mode((width, height))

    white = (255, 255, 255)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    black = (0, 0, 0)

    bg = pygame.image.load("src\img\Map3_clean_reduced.png")
    myfont = pygame.font.SysFont("Trebuchet MS", 20)
    display.blit(bg, (0, 0))

    barbare = pygame.image.load("src/img/barbare.png")
    die1 = pygame.image.load("src/img/die_1.png")
    die2 = pygame.image.load("src/img/die_2.png")
    die3 = pygame.image.load("src/img/die_3.png")
    die4 = pygame.image.load("src/img/die_4.png")
    die5 = pygame.image.load("src/img/die_5.png")
    die6 = pygame.image.load("src/img/die_6.png")

    hexagones = []
    myGrid = Grid()

    for row in range(15):
        for col in range(20):
            hex = Hexagone(col, row)
            hex.oddq_to_cube()
            hex.cube_to_axial()
            p = hex.hex_to_pixel()
            hex.q = p.x + 64
            hex.r = p.y + 90

            # label = myfont.render(str(hex.row) + "." + str(hex.col), 1, (255, 0, 0))
            # display.blit(label, (hex.q, hex.r))

            hexagones.append(hex)
            hex.draw(display, white)

    labelDice = myfont.render("Lancé du premier dé,", 1, black)
    labelDice2 = myfont.render("cliquer sur cette case", 1, black)

    launch = True

    while True:
        r = Rect(900, 25, 250, 100)
        pygame.draw.rect(display, black, r, 3)
        display.blit(labelDice, (r.left + r.width * 1 / 7, r.top + r.height * 1 / 10))
        display.blit(labelDice2, (r.left + r.width * 1 / 7, r.top + r.height * 1 / 10 + 25))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                display.blit(bg, (0, 0))

                if launch:
                    if r.left < mouse_x < (r.left + r.width) and r.top < mouse_y < (r.top + r.height):
                        dice = launchdice(1)
                        dielaunch = dice[0]

                        if dielaunch == 1:
                            dieimg = die1
                            hexdepart = Hexagone(0, 0)
                        elif dielaunch == 2:
                            dieimg = die2
                            hexdepart = Hexagone(6, 0)
                        elif dielaunch == 3:
                            dieimg = die3
                            hexdepart = Hexagone(8, 0)
                        elif dielaunch == 4:
                            dieimg = die4
                            hexdepart = Hexagone(12, 0)
                        elif dielaunch == 5:
                            dieimg = die5
                            hexdepart = Hexagone(14, 0)
                        elif dielaunch == 6:
                            dieimg = die6
                            hexdepart = Hexagone(18, 0)

                        display.blit(dieimg, (r.left + r.width * 1 / 3, r.top + r.height * 2 / 3))

                        for hex in hexagones:
                            if hexdepart.col == hex.col and hexdepart.row == hex.row:
                                hex.selected = True
                                hex.draw(display, red)

                                display.blit(barbare, (hex.q - 17 / 2, hex.r - 25 / 2))

                        launch = False
                else:
                    for hex in hexagones:
                        d = sqrt((mouse_x - hex.q) ** 2 + (mouse_y - hex.r) ** 2)
                        if d < hex.size:
                            for h in hexagones:
                                h.draw(display, white)
                                if h.selected:
                                    h.selected = False
                            hex.selected = True
                            # lstNeighbours = hex.neighbours()

                            hex.draw(display, red)

                            display.blit(barbare, (hex.q - 17 / 2, hex.r - 25 / 2))
                            break
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


main()
