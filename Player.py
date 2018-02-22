import pygame


class Player :
    def __init__(self):
        self.token = pygame.image.load("src/img/barbare.png")
        self.gold = 0
        self.health = 50

    def move(self, game, hex, move):
        if move:
            game.grid.draw_player(hex)
            game.draw_dice()
            game.current_round+=1
        else:
            for h in game.grid.hexagones:
                if h.selected:
                    game.grid.draw_player(h)

    @staticmethod
    def quote(number_quote):
        switcher = {
            "Yes": "Je me suis déplacé",
            "No": "Je ne peux pas m'y déplacer",
        }
        print(switcher.get(number_quote))
