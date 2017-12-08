import unittest
from day8.problem import *


class TestRegisters(unittest.TestCase):
    def test_real_input(self):
        result = get_max_register_from_input_file('input.txt')
        self.assertEqual(6012, result)

    def test_abs_max_register_value(self):
        result = get_abs_max_register_from_input_file('input.txt')
        self.assertEqual(6369, result)
