import unittest
import unittest.mock as mock
from counting_sort import counting_sort
from tests_data import test_values_int, test_errors, test_correct_values_int, test_negatives


class Counting_sort_tests_Case(unittest.TestCase):
    def test_with_correct_integer_values(self):
        for index, test in enumerate(test_values_int):
            self.assertEqual(counting_sort(test), (test_correct_values_int[index], mock.ANY))

    def test_error_values(self):
        with self.assertRaises(ValueError):
            for test in test_errors:
                counting_sort(test)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            for test in test_negatives:
                counting_sort(test)


if __name__ == '__main__':
    unittest.main()
