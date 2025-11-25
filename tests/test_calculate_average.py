import unittest
from first_package.calculate_average import calculate_average


class TestExample(unittest.TestCase):
    def test_calculate_average_1(self):
        temperatures1 = [37.5, 34, 39.3, 40, 38.7, 41.5]
        self.assertEqual(calculate_average(temperatures1), 38.5)

    def test_calculate_average_2(self):
        temperatures2 = [36, 37.4, 39, 41, 36.6]
        self.assertEqual(calculate_average(temperatures2), 38)

    def test_calculate_average_3(self):
        self.assertEqual(calculate_average([]), None)
