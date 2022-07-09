import unittest
import unittest.mock as mock
from quick_sort import quick_sort
from tests_data import *


class Quick_sort_test_Case(unittest.TestCase):
    def test_with_error_values(self):
        with self.assertRaises(ValueError):
            for i in test_errors:
                quick_sort(i)

    def test_with_correct_float_values(self):
        for index, test in enumerate(test_values_float):
            self.assertEqual(quick_sort(test), (test_correct_values_float[index], mock.ANY))

    def test_with_negative_values(self):
        for index, test in enumerate(test_negatives):
            self.assertEqual(quick_sort(test), (test_correct_negative_values[index], mock.ANY))

    def test_with_correct_integer_values(self):
        for index, i in enumerate(test_values_int):
            self.assertEqual(quick_sort(i), (test_correct_values_int[index], mock.ANY))


if __name__ == '__main__':
    unittest.main()
