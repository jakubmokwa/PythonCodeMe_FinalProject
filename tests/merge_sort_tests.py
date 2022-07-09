import unittest
import unittest.mock as mock
from merge_sort import merge_sort
from tests_data import *


class Merge_sort_test_Case(unittest.TestCase):
    def test_with_error_values(self):
        with self.assertRaises(ValueError):
            for i in test_errors:
                merge_sort(i)

    def test_with_correct_float_values(self):
        for index, test in enumerate(test_values_float):
            self.assertEqual(merge_sort(test), (test_correct_values_float[index], mock.ANY))

    def test_with_negative_values(self):
        for index, test in enumerate(test_negatives):
            self.assertEqual(merge_sort(test), (test_correct_negative_values[index], mock.ANY))

    def test_with_correct_integer_values(self):
        for index, i in enumerate(test_values_int):
            self.assertEqual(merge_sort(i), (test_correct_values_int[index], mock.ANY))


if __name__ == '__main__':
    unittest.main()
