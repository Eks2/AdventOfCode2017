import unittest
from mock import mock_open, patch
from day2.problem import *


class TestChecksumCalculator(unittest.TestCase):

    @patch('day2.problem.open', mock_open(read_data='5\t1\t9\t5\n7\t5\t3\n2\t4\t6\t8'), create=True)
    def test_checksum_example_1(self):
        result = calculate_checksum('this_mock_example')
        self.assertEqual(18, result)

    def test_real_checksum(self):
        result = calculate_checksum('input.txt')
        self.assertEqual(41887, result)

    @patch('day2.problem.open', mock_open(read_data='5\t9\t2\t8\n9\t4\t7\t3\n3\t8\t6\t5'), create=True)
    def test_evenly_divisible_checksum_example_1(self):
        result = calculate_evenly_divisible_checksum('this_mock_example')
        self.assertEqual(9, result)

    def test_real_evenly_divisible_checksum(self):
        result = calculate_evenly_divisible_checksum('input.txt')
        self.assertEqual(226, result)
