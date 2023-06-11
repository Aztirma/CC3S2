import unittest
from ..Produccion.Board import Board
from ..Produccion.Board import Cell
from ..Produccion.Computer import Computer

class TestComputer(unittest.TestCase):

    # AC 9.1 Movimiento del oponente computadora en el modo simple.
    def test_play_turn_simple_mode_valid_move(self):
        board = Board('P vs PC', 'Simple', 3)
        computer = Computer('P vs PC', 'Simple', 3)
        cells = board.cells
        board.turn = 'right'
        move = computer.play_turn(cells)
        self.assertIsNotNone(move)
        self.assertIsInstance(move, tuple)
        self.assertEqual(len(move), 2)
        letter, pos = move
        self.assertIn(letter, ['S', 'O'])
        x, y = pos
        self.assertLessEqual(x, 2)
        self.assertLessEqual(y, 2)
        self.assertEqual(cells[x][y].letter, ' ')

    # AC 10.1 Movimiento del oponente computadora en el modo general.
    def test_play_turn_general_mode_valid_move(self):
        board = Board('P vs PC', 'General', 3)
        computer = Computer('P vs PC', 'General', 3)
        cells = board.cells
        board.turn = 'right'
        move = computer.play_turn(cells)
        self.assertIsNotNone(move)
        self.assertIsInstance(move, tuple)
        self.assertEqual(len(move), 2)
        letter, pos = move
        self.assertIn(letter, ['S', 'O'])
        x, y = pos
        self.assertLessEqual(x, 2)
        self.assertLessEqual(y, 2)
        self.assertEqual(cells[x][y].letter, ' ')

    # AC 11.1 Jugada del computador para formar SOS.
    def test_play_turn_form_SOS(self):
        board = Board('P vs PC', 'Simple', 3)
        computer = Computer('P vs PC', 'Simple', 3)
        cells = board.cells
        cells[0][0].add_letter('S')
        cells[0][1].add_letter('O')
        board.turn = 'right'
        move = computer.play_turn(cells)
        self.assertIsNotNone(move)
        letter, pos = move
        self.assertEqual(letter, 'S')
        x, y = pos
        self.assertEqual(x, 0)
        self.assertEqual(y, 2)

    # AC 11.2 Jugada del computador sin formar SOS.
    def test_play_turn_no_possible_SOS(self):
        board = Board('P vs PC', 'Simple', 3)
        computer = Computer('P vs PC', 'Simple', 3)
        cells = board.cells
        cells[0][0].add_letter('S')
        cells[0][1].add_letter('O')
        cells[0][2].add_letter('S')
        board.turn = 'right'
        move = computer.play_turn(cells)
        self.assertIsNotNone(move)
        letter, pos = move
        self.assertIn(letter, ['S', 'O'])
        x, y = pos
        self.assertLessEqual(x, 2)
        self.assertLessEqual(y, 2)
        self.assertEqual(cells[x][y].letter, ' ')

if __name__ == '__main__':
    unittest.main()

