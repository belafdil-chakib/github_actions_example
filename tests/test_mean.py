import unittest

from funcs import mean


class TestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestSuite, cls).setUpClass()

        cls.input_numbers = list(range(1, 6))
        cls.expected_mean = 3

    def test_mean(self):
        self.assertEqual(self.expected_mean, mean(self.input_numbers))
