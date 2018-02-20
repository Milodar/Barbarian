from Point import Point
from math import *
import pygame


class Hexagone:
    def __init__(self, col, row):
        self.size = 50
        self.q = 0
        self.r = 0
        self.col = col
        self.row = row
        self.x = 0
        self.y = 0
        self.z = 0

        self.selected = False

    def draw(self, display, color):
        size = self.size
        x = self.q
        y = self.r
        height = size * 2
        width = sqrt(3) / 2 * height
        pygame.draw.polygon(display, color, (
            (x, y + size),
            (x + width / 2, y + size / 2),
            (x + width / 2, y - size / 2),
            (x, y - size),
            (x - width / 2, y - size / 2),
            (x - width / 2, y + size / 2)
        ), 3)

    def oddr_to_cube(self):
        x = self.col - (self.row - (self.row & 1)) / 2
        z = self.row
        y = -x - z
        self.x = x
        self.y = y
        self.z = z

    def cube_to_axial(self):
        q = self.x
        r = self.z
        self.q = q
        self.r = r

    def hex_to_pixel(self):
        x = self.size * sqrt(3) * (self.q + self.r / 2)
        y = self.size * 3 / 2 * self.r

        return Point(x, y)

    def pixel_to_hex(self, x, y):
        q = (x * sqrt(3) / 3 - y / 3) / self.size
        r = y * 2 / 3 / self.size
        self.q = q
        self.r = r
