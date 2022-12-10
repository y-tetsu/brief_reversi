import unittest
from short_reversi import ShortReversi


class TestShortReversi(unittest.TestCase):
    def test_play_com_vs_com(self):
        expected = [
            3, 0, 0, 0, 0, 0, 0, 0, 0,
            3, 1, 1, 1, 1, 1, 1, 1, 2,
            3, 1, 1, 1, 1, 1, 1, 1, 2,
            3, 1, 1, 1, 1, 1, 1, 1, 2,
            3, 1, 2, 1, 2, 1, 1, 1, 2,
            3, 1, 2, 1, 1, 2, 1, 1, 2,
            3, 1, 1, 2, 1, 1, 2, 1, 2,
            3, 1, 1, 1, 2, 2, 1, 2, 2,
            3, 2, 2, 2, 2, 2, 2, 2, 2,
            3, 0, 0, 0, 0, 0, 0, 0, 0,
            3]
        reversi = ShortReversi()
        reversi.play(com1=True, com2=True)
        self.assertEqual(reversi.board, expected)
