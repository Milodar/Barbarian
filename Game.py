from random import randint

import pygame
from pygame.rect import Rect

from Hexagone import Hexagone


class Game:
    def __init__(self, grid, player, number_round):
        self.player = player
        self.grid = grid
        self.max_round = number_round
        self.current_round = 0
        self.chat = Rect(900, 25, 250, 100)
        self.chat_color = (0, 0, 0)
        self.img_dice = {
                            1: pygame.image.load("src/img/die_1.png"),
                            2: pygame.image.load("src/img/die_2.png"),
                            3: pygame.image.load("src/img/die_3.png"),
                            4: pygame.image.load("src/img/die_4.png"),
                            5: pygame.image.load("src/img/die_5.png"),
                            6: pygame.image.load("src/img/die_6.png")
                        }
        self.start_pos = {
                            1: Hexagone(0, 0),
                            2: Hexagone(6, 0),
                            3: Hexagone(8, 0),
                            4: Hexagone(12, 0),
                            5: Hexagone(14, 0),
                            6: Hexagone(18, 0)
                        }
        self.status = "Not playing"

    def end(self):
        if self.current_round == self.max_round or self.player.gold >= 700:
            return False
        else:
            return True

    def end_turn(self):
        self.current_round += 1

    def test_move(self, hex):
        move = False
        for h in self.grid.hexagones:
            if h.selected:
                lst_neighbours = h.neighbours()
                for neighbour in lst_neighbours:
                    if hex.row == neighbour.row and hex.col == neighbour.col:
                        move = True
                        h.selected = False
                        hex.selected = True
                        return move
        return move

    def draw_chat(self):
        pygame.draw.rect(self.grid.display, self.chat_color, self.chat, 3)

    def game_launch(self):
        if self.status == "Not playing" or self.status == "Beginning":
            labelDice = self.grid.font.render("Lancé du premier dé,", 1, self.chat_color)
            labelDice2 = self.grid.font.render("cliquer sur cette case", 1, self.chat_color)
            self.grid.display.blit(labelDice, (self.chat.left + self.chat.width * 1 / 7, self.chat.top + self.chat.height * 1 / 10))
            self.grid.display.blit(labelDice2, (self.chat.left + self.chat.width * 1 / 7, self.chat.top + self.chat.height * 1 / 10 + 25))
            if self.status == "Beginning":
                self.status = "Playing"

    def draw_dice(self):
            dice = self.launchdice(1)
            dielaunch = dice[0]
            dieimg = self.img_dice.get(dielaunch)

            self.grid.draw_dice(dieimg, self.chat)

    def start(self, mouse_x, mouse_y):
        if self.chat.left < mouse_x < (self.chat.left + self.chat.width) and self.chat.top < mouse_y < (self.chat.top + self.chat.height):
            dice = self.launchdice(1)
            dielaunch = dice[0]
            player_start = self.start_pos.get(dielaunch)
            dieimg = self.img_dice.get(dielaunch)

            self.grid.draw_dice(dieimg, self.chat)
            for hex in self.grid.hexagones:
                if player_start.col == hex.col and player_start.row == hex.row:
                    hex.selected = True
                    self.grid.draw_player(hex)
        self.status = "Beginning"


    @staticmethod
    def launchdice(nbdice):
        dice = []
        for i in range(nbdice):
            die = randint(1, 6)
            dice.append(die)
        return dice
