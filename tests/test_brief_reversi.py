import unittest
from brief_reversi import reversi


class TestBriefRevers(unittest.TestCase):
    def test_com_vs_com(self):
        expected = [
            0, 0, 0, 0, 0, 0, 0, 0, 0,
            3, 1, 1, 1, 1, 1, 1, 1, 2,
            3, 1, 1, 1, 1, 1, 1, 1, 2,
            3, 1, 1, 1, 1, 1, 1, 1, 2,
            3, 1, 2, 1, 2, 1, 1, 1, 2,
            3, 1, 2, 1, 1, 2, 1, 1, 2,
            3, 1, 1, 2, 1, 1, 2, 1, 2,
            3, 1, 1, 1, 2, 2, 1, 2, 2,
            3, 2, 2, 2, 2, 2, 2, 2, 2,
            3, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        board = [0] * 91
        board[40] = board[50] = 1
        board[41] = board[49] = 2
        for i in range(1, 10):
            board[i*9] = 3
        self.assertEqual(reversi(board, 1, True, True), expected)
