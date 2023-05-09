class Computer:
    def make_turn(self, cells):
        empty_cells = []

        for i in range(cells):
            for j in range(cells[0]):
                if cells[i][j].letter == '':
                    empty_cells.append((i, j))

        if len(empty_cells) > 0:
            for pos in empty_cells:
                copy_cells = cells.copy()
                