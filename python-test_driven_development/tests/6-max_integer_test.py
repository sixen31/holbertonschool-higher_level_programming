#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for unittest with

    Module that tests correct input
    Module that tests empty list
    Module that tests input types
    """

    def test_correct_input(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -4, -3]), -1)
        self.assertEqual(max_integer([-1, 3, -4, 2]), 3)
        self.assertEqual(max_integer([1, 5.4, 4, -2]), 5.4)
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer([-5]), -5)
        self.assertEqual(max_integer([1, 1]), 1)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_input_types(self):
        self.assertRaises(TypeError, max_integer, ["str", 2, 3])
        self.assertRaises(TypeError, max_integer, [True, "str", 3])
        self.assertEqual(max_integer(False), False)
        self.assertEqual(max_integer([False, True, 3]), 3)
        self.assertEqual(max_integer("higher ASCII value is : v"), "v")


if __name__ == '__main__':
    unittest.main()
