import unittest
from day6.problem import *


class TestRedistributionAlgorithms(unittest.TestCase):

    def test_example_1(self):
        result1, result2 = redistribution_cycles_to_same_result([0, 2, 7, 0])
        self.assertEqual(5, result1)
        self.assertEqual(4, result2)

    def test_real_puzzle_input(self):
        result1, result2 = redistribution_cycles_to_same_result([5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 6])
        self.assertEqual(5042, result1)
        self.assertEqual(1086, result2)
