import unittest
from ..Produccion.Board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board('PVP', 'General', 3)

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
