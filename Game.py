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
                for neighbour in lst_neighbours:
                    if hex.row == neighbour.row and hex.col == neighbour.col:
                        move = True
                        h.selected = False
                        hex.selected = True
                        return move
        return move
