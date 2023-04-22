letters = [' ', 'S', 'O']
gamemodes_1 = ['PVP', 'PVE']
gamemodes_2 = ['Simple', 'General']
sizes = range(3, 16)


class Cell:
    def __init__(self):
        self.letter = ' '

    def add_letter(self, letter):
        if letter in letters[1:]:
            self.letter = letter

    def is_empty(self):
        return self.letter == ' '


class Board:
    def __init__(self, gamemode_1, gamemode_2, size):
        self.gamemode_1 = gamemode_1 if gamemode_1 in gamemodes_1 else None
        self.gamemode_2 = gamemode_2 if gamemode_2 in gamemodes_2 else None
        self.size = size if size in sizes else None
        if size is not None:
            self.cells = [[Cell() for i in range(size)] for j in range(size)]
