import unittest

from funcs import mean


class TestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestSuite, cls).setUpClass()

        cls.input_numbers_1 = list(range(1, 6))
        cls.expected_mean_1 = 3

    cls.input_numbers_2 = list(range(1, 5))
    cls.expected_mean_2 = 2.5

    cls.input_numbers_3 = list(1)
    cls.expected_mean_3 = 1
    
    def test_mean(self):
        self.assertEqual(self.expected_mean_1, mean(self.input_numbers_1))
        self.assertEqual(self.expected_mean_2, mean(self.input_numbers_2))
        self.assertEqual(self.expected_mean_3, mean(self.input_numbers_3))
