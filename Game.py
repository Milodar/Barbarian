class Game:
    def __init__(self, grid, player, number_round ):
        self.player = player
        self.grid = grid
        self.max_round = number_round
        self.current_round = 0

    def end(self):
        if self.current_round == self.max_round or self.player.gold >= 700:
            return True
        else:
            return False

    def end_turn(self):
        self.current_round += 1

    def test_move(self, hex):
        move = False
        for h in self.grid.hexagones:
            if h.selected:
                lst_neighbours = h.neighbours()
                length = lst_neighbours.__len__()
                for i in range(length):
                    neighbour_player = lst_neighbours[i]
                    neighbour_player_row = neighbour_player.row
                    neighbour_player_col = neighbour_player.col
                    #print(str(i) + " : [" + str(neighbour_player_row) + ";" + str(
                    #    neighbour_player_col) + "]")
                    if hex.row == neighbour_player_row and hex.col == neighbour_player_col:
                        move = True
                        h.selected = False
                        hex.selected = True
                        #print("Neighbour : " + str(i) + " -- Row : " + str(
                        #    neighbour_player.row) + " | Col : " + str(neighbour_player.col))
        return move
