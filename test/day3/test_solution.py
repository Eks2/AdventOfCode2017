import unittest
from day3.problem import *


class TestSpiralMemory(unittest.TestCase):

    def test_find_steps_from_number(self):
        result = find_steps_from_number(277678)
        self.assertEqual(475, result)

    def test_find_next_sum_value_in_spiral_memory(self):
        result = find_next_sum_value_in_spiral_memory(277678)
        self.assertEqual(279138, result)

