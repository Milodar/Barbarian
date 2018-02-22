import pygame


class Player :
    def __init__(self):
        self.token = pygame.image.load("src/img/barbare.png")
        self.gold = 0

    def move(self, game, hex):
        move = game.test_move(hex)

        if move:
            game.grid.draw_player(hex)
            Player.quote("Yes")
        else:
            for h in game.grid.hexagones:
                if h.selected:
                    game.grid.draw_player(h)

                    Player.quote("No")

    @staticmethod
    def quote(number_quote):
        switcher = {
            "Yes": "Je me suis déplacer",
            "No": "Je ne peux pas m'y déplacer",
        }
        print(switcher.get(number_quote))
