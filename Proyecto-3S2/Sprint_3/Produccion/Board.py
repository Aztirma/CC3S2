letters = ['-', 'S', 'O']
gamemodes_1 = ['Singleplayer', 'Multiplayer']
gamemodes_2 = ['Simple', 'General']
players = ['Blue', 'Red']
sizes = range(3, 17)


class Cell:
    def __init__(self):
        self.letter = '-'

    def add_letter(self, letter):
        if letter in letters[1:]:
            self.letter = letter

    def is_empty(self):
        return self.letter == '-'


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
            else:
                return "Game started"

    def change_turn(self):
        self.turn = players[0] if self.turn == players[1] else players[1]

    def add_letter(self, letter, pos_x, pos_y):
        if self.cells[pos_x][pos_y].letter == ' ':
            self.cells[pos_x][pos_y].add_letter(letter)
            self.change_turn()
            return True
        return False

    def check_SOS(self, letter, x, y):
        SOS = []
        super_grid = [[Cell() for i in range(self.size + 4)] for j in range(self.size + 4)]
        for i in range(self.size):
            for j in range(self.size):
                super_grid[i + 2][j + 2] = self.cells[i][j]
        two_distance = [(x - 2, y - 2), (x + 2, y + 2), (x, y - 2), (x, y + 2),
                        (x + 2, y - 2), (x - 2, y + 2), (x - 2, y), (x + 2, y)]
        one_distance = [(x - 1, y - 1), (x + 1, y + 1), (x, y - 1), (x, y + 1),
                        (x + 1, y - 1), (x - 1, y + 1), (x - 1, y), (x + 1, y)]
        if letter == 'S':
            for e, c in zip(two_distance, one_distance):
                
                if super_grid[e[0]][e[1]] == 'S' and super_grid[c[0]][c[1]] == 'O':
                    SOS.append([(e[0], e[1]), (x, y)])
        elif letter == 'O':
            for e1, e2 in zip(one_distance[::2], one_distance[1::2]):
                if super_grid[e1[0]][e1[1]] == 'S' and super_grid[e2[0]][e2[1]] == 'S':
                    SOS.append([(e1[0], e1[1]), (e2[0], e2[1])])
        print(SOS != [])
        return SOS != [], SOS

    def print_console(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.cells[i][j].letter, ' ', end='')
            print()
