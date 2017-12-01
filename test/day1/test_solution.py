import unittest
from day1.problem import *


class TestCaptchaSolver(unittest.TestCase):

    def test_example_1(self):
        input_string = '1122'
        result = captcha_solver(input_string)
        self.assertEqual(3, result)

    def test_example_2(self):
        input_string = '1111'
        result = captcha_solver(input_string)
        self.assertEqual(4, result)

    def test_example_3(self):
        input_string = '1234'
        result = captcha_solver(input_string)
        self.assertEqual(0, result)

    def test_example_4(self):
        input_string = '91212129'
        result = captcha_solver(input_string)
        self.assertEqual(9, result)

    def test_example_5(self):
        input_string = '111222333'
        result = captcha_solver(input_string)
        self.assertEqual(12, result)

    def test_real_captcha(self):
        with open('input.txt', 'r') as f:
            input_string = f.read()
        result = captcha_solver(input_string)
        self.assertEqual(1136, result)

    def test_lookahead_captcha_solver_example_1(self):
        input_string = '1122'
        result = lookahead_captcha_solver(input_string)
        self.assertEqual(3, result)

    def test_lookahead_captcha_solver_example_1(self):
        input_string = '1111'
        result = lookahead_captcha_solver(input_string)
        self.assertEqual(4, result)

    def test_lookahead_captcha_solver_example_2(self):
        input_string = '1234'
        result = lookahead_captcha_solver(input_string)
        self.assertEqual(0, result)

    def test_lookahead_captcha_solver_example_3(self):
        input_string = '91212129'
        result = lookahead_captcha_solver(input_string)
        self.assertEqual(9, result)

    def test_lookahead_captcha_solver_example_4(self):
        input_string = '111222333'
        result = lookahead_captcha_solver(input_string)
        self.assertEqual(12, result)

    def test_lookahead_captcha_solver_example_5(self):
        with open('input.txt', 'r') as f:
            input_string = f.read()
        result = captcha_solver(input_string)
        self.assertEqual(1136, result)

    def test_half_list_lookahead_captcha_solver_example_6(self):
        input_string = '1212'
        result = half_list_lookahead_captcha_solver(input_string)
        self.assertEqual(6, result)

    def test_half_list_lookahead_captcha_solver_example_7(self):
        input_string = '1221'
        result = half_list_lookahead_captcha_solver(input_string)
        self.assertEqual(0, result)

    def test_half_list_lookahead_captcha_solver_example_8(self):
        input_string = '123425'
        result = half_list_lookahead_captcha_solver(input_string)
        self.assertEqual(4, result)

    def test_half_list_lookahead_captcha_solver_example_9(self):
        input_string = '123123'
        result = half_list_lookahead_captcha_solver(input_string)
        self.assertEqual(12, result)

    def test_half_list_lookahead_captcha_solver_example_10(self):
        input_string = '12131415'
        result = half_list_lookahead_captcha_solver(input_string)
        self.assertEqual(4, result)

    def test_real_half_list_lookahead_captcha(self):
        with open('input.txt', 'r') as f:
            input_string = f.read()
        result = half_list_lookahead_captcha_solver(input_string)
        self.assertEqual(1092, result)
