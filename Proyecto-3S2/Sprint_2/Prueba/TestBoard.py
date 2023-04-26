import unittest
from ..Produccion.Board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.simple_board = Board('Multiplayer', 'Simple', 8)
        self.general_board = Board('Multiplayer', 'General', 6)
        self.incorrect_board = Board('Multiplayer', 'Simple', 2)

    # AC 1.2. Elección correcta del tamaño del tablero
    def test_correct_board_size(self):
        self.assertEqual(self.simple_board.start_game(), 'Game started')
        self.assertEqual(self.general_board.start_game(), 'Game started')

    # AC 1.3. Elección incorrecta del tamaño del tablero
    def test_incorrect_board_size(self):
        self.assertEqual(self.incorrect_board.start_game(), 'Board size invalid.')

    # AC 2.1. Elección del modo de juego simple
    def test_simple_mode(self):
        self.assertEqual(self.simple_board.gamemode_2, 'Simple')

    # AC 2.2. Elección del modo de juego general
    def test_general_mode(self):
        self.assertEqual(self.general_board.gamemode_2, 'General')

    # AC 4.2. Realizar un movimiento en el modo simple
    def test_correct_add_letter_simple(self):
        self.simple_board.add_letter('S', 0, 0)
        self.assertEqual(self.simple_board.cells[0][0].letter, 'S')

        self.simple_board.add_letter('O', 1, 1)
        self.assertEqual(self.simple_board.cells[1][1].letter, 'O')

    # AC 4.3. Realizar un movimiento fallido en el modo simple
    def test_incorrect_add_letter_simple(self):
        self.simple_board.add_letter('S', 0, 0)
        self.assertEqual(self.simple_board.turn, 'Red')
        self.simple_board.add_letter('O', 0, 0)
        self.assertEqual(self.simple_board.turn, 'Red')
        self.assertEqual(self.simple_board.cells[0][0].letter, 'S')

    # AC 6.2. Realizar un movimiento en el modo general
    def test_correct_add_letter_general(self):
        self.general_board.add_letter('S', 0, 0)
        self.assertEqual(self.general_board.cells[0][0].letter, 'S')

        self.general_board.add_letter('O', 1, 1)
        self.assertEqual(self.general_board.cells[1][1].letter, 'O')

    # AC 6.4. Realizar un movimiento fallido en el modo general
    def test_incorrect_add_letter_general(self):
        self.general_board.add_letter('S', 0, 0)
        self.assertEqual(self.general_board.turn, 'Red')
        self.general_board.add_letter('O', 0, 0)
        self.assertEqual(self.general_board.turn, 'Red')
        self.assertEqual(self.general_board.cells[0][0].letter, 'S')


if __name__ == '__main__':
    unittest.main()
