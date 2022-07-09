import unittest
import unittest.mock as mock
from bubble_sort import bubble_sort
from tests_data import test_values, correct_test_values, test_errors


class MyTestCase(unittest.TestCase):
    def test_bubble_sort_with_wrong_types(self):
        with self.assertRaises(ValueError):
            for i in test_errors:
                bubble_sort(i)

    def test_bubble_sort_with_correct_values(self):
        for index, i in enumerate(test_values):
            self.assertEqual(bubble_sort(i), (correct_test_values[index], mock.ANY))


if __name__ == '__main__':
    unittest.main()
