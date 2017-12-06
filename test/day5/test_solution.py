import unittest
from day5.problem import *


class TestMazePuzzle(unittest.TestCase):
    def test_steps_to_exit(self):
        result = steps_to_exit([0, 3, 0, 1, -3])
        self.assertEqual(5, result)

    def test_real_steps_to_exit(self):
        result = file_input_steps_to_exit('input.txt')
        self.assertEqual(351282, result)

    def test_strange_steps_to_exit(self):
        result = steps_to_exit([0, 3, 0, 1, -3], True)
        self.assertEqual(10, result)

    def test_real_strange_steps_to_exit(self):
        result = steps_to_exit('input.txt', True)
        self.assertEqual(24568703, result)
