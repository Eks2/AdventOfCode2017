import unittest
from day4.problem import *


class TestPassphraseValidator(unittest.TestCase):

    def test_is_passphrase_valid(self):
        result = is_passphrase_valid('aa bb cc dd ee')
        self.assertEqual(True, result)

    def test_is_passphrase_valid(self):
        result = is_passphrase_valid('aa bb cc dd aa')
        self.assertEqual(False, result)

    def test_is_passphrase_valid(self):
        result = is_passphrase_valid('aa bb cc dd aaa')
        self.assertEqual(True, result)

    def test_real_number_of_valid_passphrases(self):
        result = number_of_valid_passphrases('input.txt')
        self.assertEqual(325, result)

    def test_real_number_of_extra_security_valid_passphrases(self):
        result = number_of_extra_security_valid_passphrases('input.txt')
        self.assertEqual(119, result)
