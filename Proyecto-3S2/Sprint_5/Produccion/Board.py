letters = [' ', 'S', 'O']
gamemodes_1 = ['P vs PC', 'P vs P', 'PC vs PC']
gamemodes_2 = ['Simple', 'General']
players = ['left', 'right']
sizes = range(3, 17)


class Cell:
    def __init__(self):
        self.letter = letters[0]

    def add_letter(self, letter):
        if letter in letters[1:]:
            self.letter = letter

    def is_empty(self):
        return self.letter == letters[0]


class Board:
    def __init__(self, gamemode_1, gamemode_2, size):
        self.gamemode_1 = gamemode_1 if gamemode_1 in gamemodes_1 else None
        self.gamemode_2 = gamemode_2 if gamemode_2 in gamemodes_2 else None
        self.size = size if size in sizes else None
        if size is not None:
            self.cells = [[Cell() for i in range(size)] for j in range(size)]
        self.turn = players[0]
        self.SOS_created = {players[0]: 0, players[1]: 0}
        #SPRINT4
        self.moves = []  # Lista para almacenar los movimientos del juego

    def start_game(self):
        if self.gamemode_1 is not None and self.gamemode_2 is not None:
            if self.size is None:
                return "Board size invalid."
            else:
                return "Game started"

    def change_turn(self):
        self.turn = players[0] if self.turn == players[1] else players[1]

    def add_letter(self, letter, pos_x, pos_y):
        if not self.cells[pos_x][pos_y].is_empty():
            print("Invalid move. Cell already contains a letter:", self.cells[pos_x][pos_y].letter)
            return False

        self.cells[pos_x][pos_y].add_letter(letter)
        move_info = 'Turno: {} - Letra: {} - Fila: {} - Columna: {}'.format(self.turn, letter, pos_x, pos_y)
        self.moves.append(move_info)
        return True

    def check_SOS(self, letter, x, y):
        SOS = []
        super_grid = [[Cell() for i in range(self.size + 4)] for j in range(self.size + 4)]
        for i in range(self.size):
            for j in range(self.size):
                super_grid[i + 2][j + 2].letter = self.cells[i][j].letter
        x += 2
        y += 2
        two_distance = [(x - 2, y - 2), (x + 2, y + 2), (x, y - 2), (x, y + 2),
                        (x + 2, y - 2), (x - 2, y + 2), (x - 2, y), (x + 2, y)]
        one_distance = [(x - 1, y - 1), (x + 1, y + 1), (x, y - 1), (x, y + 1),
                        (x + 1, y - 1), (x - 1, y + 1), (x - 1, y), (x + 1, y)]
        if letter == 'S':
            for e, c in zip(two_distance, one_distance):
                if super_grid[e[0]][e[1]].letter == 'S' and super_grid[c[0]][c[1]].letter == 'O':
                    SOS.append([(e[0] - 2, e[1] - 2), (x - 2, y - 2)])
        elif letter == 'O':
            for e1, e2 in zip(one_distance[::2], one_distance[1::2]):
                if super_grid[e1[0]][e1[1]].letter == 'S' and super_grid[e2[0]][e2[1]].letter == 'S':
                    SOS.append([(e1[0] - 2, e1[1] - 2), (e2[0] - 2, e2[1] - 2)])
        self.SOS_created[self.turn] += len(SOS)
        return SOS != [], SOS

    def isBoardFull(self):
        for row in self.cells:
            for cell in row:
                if cell.is_empty():
                    return False
        return True

    def checkVictory(self):
        if self.gamemode_2 == 'Simple':
            if self.SOS_created[players[0]] > 0:
                return players[0]
            if self.SOS_created[players[1]] > 0:
                return players[1]
            if self.isBoardFull():
                return 'Draw'
            return None
        if self.gamemode_2 == 'General':
            if self.isBoardFull():
                if self.SOS_created[players[0]] > self.SOS_created[players[1]]:
                    return players[0]
                if self.SOS_created[players[1]] > self.SOS_created[players[0]]:
                    return players[1]
                return 'Draw'
            return None

    def print_console(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.cells[i][j].letter, ' ', end='')
            print()

    def record_game(self, filename):
        if self.start_game() != "Game started":
            return "Cannot record game. Game has not started."
        if not self.moves:
            return "No moves to record."

        sos_created = set()  # Utilizamos un conjunto para evitar duplicados

        try:
            with open(filename, 'w') as file:
                file.write("Gamemode 1: {}\n".format(self.gamemode_1))
                file.write("Gamemode 2: {}\n".format(self.gamemode_2))
                file.write("Tamaño del tablero: {}\n".format(self.size)+"\n")
                for move in self.moves:
                    info = move.split(" - ")
                    if len(info) != 4:
                        return "Invalid move format."

                    pos_x = int(info[2].split(":")[1].strip())
                    pos_y = int(info[3].split(":")[1].strip())
                    letter = info[1].split(":")[1].strip()

                    if letter == 'S':
                        sos_result = self.check_SOS(letter, pos_x, pos_y)
                        if sos_result[0]:
                            for sos in sos_result[1]:
                                sos_created.add(
                                    tuple(sorted(sos)))  # Convertimos a una tupla ordenada para evitar duplicados

                    file.write(move + '\n')

                # Escribir los SOS creados en el archivo de texto
                if sos_created:
                    file.write("\nSOS created:\n")
                    for sos in sos_created:
                        file.write("SOS: {}\n".format(sos))

            return "Game recorded successfully."
        except IOError:
            return "Error occurred while recording the game."