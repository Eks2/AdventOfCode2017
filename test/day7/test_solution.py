import unittest
from day7.problem import *


class TestTowerStructure(unittest.TestCase):

    def test_real_example(self):
        result = build_tower_stack_from_file('input.txt')
        self.assertEqual('hmvwl', result.name)
