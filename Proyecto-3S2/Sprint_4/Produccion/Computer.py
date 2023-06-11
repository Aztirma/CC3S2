import random
from .Board import *


class Computer:
    def __init__(self, gamemode_1, gamemode_2, size):
        self.gamemode_1 = gamemode_1
        self.gamemode_2 = gamemode_2
        self.size = size

    @staticmethod
    def get_empty_cells(cells):
        empty_cells = []
        for i in range(len(cells)):
            for j in range(len(cells[0])):
                if cells[i][j].letter == ' ':
                    empty_cells.append((i, j))
        return empty_cells

    @staticmethod
    def copy_cells(cells):
        copy_cells = [[Cell() for _ in range(len(cells))] for _ in range(len(cells[0]))]
        for i in range(len(cells)):
            for j in range(len(cells[0])):
                copy_cells[i][j].letter = cells[i][j].letter
        return copy_cells

    def play_turn(self, cells):
        candidate_plays = self.check_possible_SOS(cells)
        if len(candidate_plays) > 0:
            return random.choice(candidate_plays)

        empty_cells = Computer.get_empty_cells(cells)
        candidate_plays = []

        for pos in empty_cells:
            for letter in ['S', 'O']:
                copy_cells = Computer.copy_cells(cells)
                copy_cells[pos[0]][pos[1]].add_letter(letter)

                if len(self.check_possible_SOS(copy_cells)) == 0:
                    candidate_plays.append((letter, pos))

        if len(candidate_plays) > 0:
            return random.choice(candidate_plays)

        if len(empty_cells) > 0:
            return random.choice(empty_cells)

        return None

    def check_possible_SOS(self, cells):
        empty_cells = Computer.get_empty_cells(cells)

        candidate_plays = []
        for pos in empty_cells:
            for letter in ['S', 'O']:
                copy_cells = Computer.copy_cells(cells)
                copy_cells[pos[0]][pos[1]].add_letter(letter)
                board = Board(self.gamemode_1, self.gamemode_2, self.size)
                board.cells = copy_cells
                createdSOS, _ = board.check_SOS(letter, pos[0], pos[1])
                if createdSOS:
                    candidate_plays.append((letter, pos))
        return candidate_plays