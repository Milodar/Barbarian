from Point import Point
from math import *
import pygame


class Hexagone:
    def __init__(self, col, row):
        self.size = 25
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
            (x + size, y),
            (x + size / 2, y + width / 2),
            (x - size / 2, y + width / 2),
            (x - size, y),
            (x - size / 2, y - width / 2),
            (x + size / 2, y - width / 2)
        ), 3)

    def oddq_to_cube(self):
        x = self.col
        z = self.row - (self.col - (self.col & 1)) / 2
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
        x = self.size * 3/2 * self.q
        y = self.size * sqrt(3) * (self.r + self.q/2)

        return Point(x, y)

    def pixel_to_hex(self, x, y):
        q = x * 2/3 / self.size
        r = (-x / 3 + sqrt(3)/3 * y) / self.size
        self.q = q
        self.r = r
