letters = [' ', 'S', 'O']
gamemodes_1 = ['Singleplayer', 'Multiplayer']
gamemodes_2 = ['Simple', 'General']
players = ['Blue', 'Red']
sizes = range(3, 17)


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
        self.turn = players[0]

    def start_game(self):
        if self.gamemode_1 is not None and self.gamemode_2 is not None:
            if self.size is None:
                return "Board size invalid."
            return "Game started"
        return "Gamemode invalid"

    def change_turn(self):
        self.turn = players[0] if self.turn == players[1] else players[1]

    def add_letter(self, letter, pos_x, pos_y):
        if self.cells[pos_x][pos_y].letter == ' ':
            self.cells[pos_x][pos_y].add_letter(letter)
            self.change_turn()
            return True
        return False

    def print_console(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.cells[i][j].letter, ' ', end='')
            print()
