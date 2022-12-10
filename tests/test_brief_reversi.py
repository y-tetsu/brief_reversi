import unittest
from brief_reversi import BriefReversi


class TestBriefRevers(unittest.TestCase):
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
        reversi = BriefReversi()
        reversi.play(com1=True, com2=True)
        self.assertEqual(reversi.board, expected)
