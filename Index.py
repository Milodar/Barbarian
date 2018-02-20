import os, sys
import pygame as pg  # lazy but responsible (avoid namespace flooding)

import time

x = 0
y = 0


def main(Surface):
    game_event_loop()
    blue = (0, 255, 255)
    pg.draw.rect(Surface, blue, (x, y, 100, 50))


def game_event_loop():
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            Mouse_x, Mouse_y = pg.mouse.get_pos()
            print(" CLICK ")
            print(Mouse_x)
            print(Mouse_y)
        elif event.type == pg.MOUSEBUTTONUP:
            print(" CLICK UP")
        elif event.type == pg.QUIT:
            print(" QUIT")


pg.init()
Screen = pg.display.set_mode((500, 400), 0, 32)

while 1:
    x += 1

    y += 1
    main(Screen)
    pg.display.update()
    time.sleep(.300)
