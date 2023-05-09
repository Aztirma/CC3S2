import random


class Computer:
    @staticmethod
    def play_turn(cells):
        empty_cells = []

        for i in range(cells):
            for j in range(cells[0]):
                if cells[i][j].letter == ' ':
                    empty_cells.append((i, j))

        candidate_plays = Computer.check_possible_SOS(cells)
        if len(candidate_plays) > 0:
            return random.choice(candidate_plays)

        for pos in empty_cells:
            copy_cells = cells.copy()
            copy_cells[pos[0]][pos[1]].add_letter('S')
            if len(Computer.check_possible_SOS(copy_cells)) == 0:
                candidate_plays.append(('S', pos))
            copy_cells = cells.copy()
            copy_cells[pos[0]][pos[1]].add_letter('O')
            if len(Computer.check_possible_SOS(copy_cells)) == 0:
                candidate_plays.append(('O', pos))

        if len(candidate_plays) > 0:
            return random.choice(candidate_plays)

        for pos in empty_cells:
            candidate_plays.append(('S', pos))
            candidate_plays.append(('O', pos))
        return random.choice(candidate_plays)

    @staticmethod
    def check_possible_SOS(cells):
        return []
