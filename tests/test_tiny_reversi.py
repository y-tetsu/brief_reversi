import unittest
from tiny_reversi import reversi


class TestTinyRevers(unittest.TestCase):
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
        self.assertEqual(reversi(True), expected)
