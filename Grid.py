from Terrain import Terrain as t
from Hexagone import Hexagone


class Grid:
    def __init__(self, row_grid, col_grid, display, clear_color, player_color, player_token, start_pos):
        self.terrain = [
            [t(1), t(6), t(6), t(4), t(4), t(1), t(1), t(3), t(6), t(3), t(3), t(4), t(1), t(5), t(2), t(2), t(3), t(6), t(6), t(6)],
            [t(1), t(4), t(4), t(4), t(1), t(1), t(1), t(4), t(1), t(4), t(3), t(4), t(5), t(1), t(5), t(1), t(3), t(6), t(6), t(6)],
            [t(6), t(4), t(4), t(6), t(6), t(6), t(6), t(4), t(4), t(3), t(5), t(3), t(1), t(1), t(4), t(6), t(6), t(1), t(6), t(3)],
            [t(1), t(3), t(6), t(6), t(6), t(1), t(1), t(6), t(3), t(1), t(1), t(6), t(4), t(4), t(4), t(4), t(1), t(6), t(3), t(1)],
            [t(3), t(3), t(1), t(6), t(4), t(3), t(4), t(4), t(1), t(1), t(6), t(1), t(1), t(3), t(6), t(6), t(6), t(6), t(1), t(3)],
            [t(7), t(7), t(7), t(3), t(3), t(4), t(1), t(3), t(1), t(6), t(6), t(6), t(3), t(3), t(6), t(7), t(6), t(6), t(1), t(6)],
            [t(3), t(3), t(3), t(7), t(1), t(1), t(1), t(4), t(1), t(4), t(3), t(6), t(6), t(7), t(7), t(7), t(7), t(6), t(6), t(3)],
            [t(1), t(1), t(1), t(4), t(4), t(1), t(1), t(4), t(4), t(1), t(3), t(3), t(7), t(7), t(7), t(7), t(7), t(3), t(6), t(6)],
            [t(1), t(1), t(4), t(4), t(4), t(5), t(4), t(4), t(1), t(2), t(3), t(3), t(7), t(7), t(7), t(7), t(3), t(6), t(6), t(3)],
            [t(1), t(1), t(4), t(1), t(1), t(4), t(5), t(1), t(1), t(3), t(1), t(1), t(3), t(3), t(7), t(3), t(7), t(6), t(6), t(3)],
            [t(4), t(1), t(1), t(5), t(5), t(5), t(4), t(4), t(4), t(3), t(6), t(6), t(6), t(3), t(3), t(6), t(3), t(3), t(1), t(6)],
            [t(1), t(1), t(5), t(1), t(1), t(1), t(4), t(4), t(3), t(1), t(3), t(6), t(4), t(3), t(3), t(3), t(6), t(3), t(3), t(6)],
            [t(1), t(5), t(5), t(1), t(4), t(1), t(5), t(4), t(4), t(1), t(3), t(1), t(6), t(4), t(1), t(1), t(3), t(3), t(3), t(3)],
            [t(5), t(5), t(4), t(4), t(4), t(1), t(1), t(4), t(5), t(1), t(6), t(6), t(1), t(2), t(1), t(1), t(1), t(1), t(1), t(1)],
            [t(5), t(4), t(4), t(1), t(1), t(1), t(4), t(4), t(4), t(5), t(1), t(3), t(1), t(2), t(2), t(1), t(4), t(4), t(1), t(4)],
            [t(4), t(1), t(1), t(1), t(4), t(1), t(4), t(1), t(2), t(1), t(1), t(1), t(2), t(1), t(1), t(1), t(4), t(1), t(4), t(1)]
        ]
        self.hexagones = []
        self.display = display
        self.clear_color = clear_color
        self.player_color = player_color
        self.player_token = player_token
        self.start_pos_row = start_pos.row
        self.start_pos_col = start_pos.col

        for row in range(row_grid):
            for col in range(col_grid):
                hex = Hexagone(col, row)
                hex.oddq_to_cube()
                hex.cube_to_axial()
                p = hex.hex_to_pixel()
                hex.q = p.x + 64
                hex.r = p.y + 90
                if row == start_pos.row and col == start_pos.col:
                    hex.selected = True
                self.hexagones.append(hex)

    def move(self, hex):
        move = False
        for h in self.hexagones:
            h.draw(self.display, self.clear_color)
            if h.selected:
                lstNeighbours = h.neighbours()
                compteur = lstNeighbours.__len__()
                for i in range(compteur):
                    neighbourplayer = lstNeighbours[i]
                    neighbourplayer_row = neighbourplayer.row
                    neighbourplayer_col = neighbourplayer.col
                    print(str(i) + " : [" + str(neighbourplayer_row) + ";" + str(
                        neighbourplayer_col) + "]")
                    if hex.row == neighbourplayer_row and hex.col == neighbourplayer_col:
                        move = True
                        h.selected = False
                        print("Neighbour : " + str(i) + " -- Row : " + str(
                            neighbourplayer.row) + " | Col : " + str(neighbourplayer.col))

        if move:
            hex.selected = True
            hex.draw(self.display, self.player_color)
            self.display.blit(self.player_token, (hex.q - 17 / 2, hex.r - 25 / 2))
        else:
            for h in self.hexagones:
                if h.selected:
                    h.draw(self.display, self.player_color)
                    self.display.blit(self.player_token, (h.q - 17 / 2, h.r - 25 / 2))
