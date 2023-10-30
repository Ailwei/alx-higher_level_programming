#!/usr/bin/python3

#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]), "Empty list should return None")

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5, "Single element list should return that element")

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4, "Max in [1, 2, 3, 4] is 4")

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1, "Max in [-1, -2, -3, -4] is -1")

    def test_mixed_positive_negative_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4, "Max in [-1, 2, -3, 4] is 4")

    def test_duplicate_max(self):
        self.assertEqual(max_integer([1, 3, 4, 4]), 4, "Max in [1, 3, 4, 4] is 4")

if __name__ == "__main__":
    unittest.main()
