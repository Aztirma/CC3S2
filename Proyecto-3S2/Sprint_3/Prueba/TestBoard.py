import unittest
from ..Produccion.Board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board('PVP', 'General', 8)
        self.incorrect_board = Board('Simple', 'Multiplayer', 2)

    def test_incorrect_board_size(self):
        self.assertEqual(self.incorrect_board.start_game(), 'Board size invalid.')

    def test_change_turn(self):
        self.assertEqual(self.board.turn, 'Blue')
        self.board.change_turn()
        self.assertEqual(self.board.turn, 'Red')
        self.board.change_turn()
        self.assertEqual(self.board.turn, 'Blue')

    def test_add_letter(self):
        self.board.add_letter('S', 0, 0)
        self.assertEqual(self.board.cells[0][0].letter, 'S')
        self.assertEqual(self.board.turn, 'Red')

        self.board.add_letter('O', 0, 0)
        self.assertEqual(self.board.cells[0][0].letter, 'S')
        self.assertEqual(self.board.turn, 'Red')


if __name__ == '__main__':
    unittest.main()
