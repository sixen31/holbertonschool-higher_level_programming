#!/usr/bin/python3
"""
Unit tests for the Rectangle class.
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_to_dictionary(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        rect_dict = r1.to_dictionary()
        self.assertEqual(rect_dict, {
            'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4
        })

    def test_to_dictionary_empty(self):
        r2 = Rectangle(1, 1)
        rect_dict = r2.to_dictionary()
        self.assertEqual(rect_dict, {
            'id': 1, 'width': 1, 'height': 1, 'x': 0, 'y': 0
        })

    def test_to_dictionary_large_values(self):
        r3 = Rectangle(99999, 99999, 99999, 99999, 99999)
        rect_dict = r3.to_dictionary()
        self.assertEqual(rect_dict, {
            'id': 99999, 'width': 99999, 'height':
            99999, 'x': 99999, 'y': 99999
        })

    def test_to_dictionary_zero_values(self):
        r4 = Rectangle(0, 0, 0, 0, 0)
        rect_dict = r4.to_dictionary()
        self.assertEqual(rect_dict, {
            'id': 0, 'width': 0, 'height': 0, 'x': 0, 'y': 0
        })

    def test_to_dictionary_negative_values(self):
        r5 = Rectangle(-1, -2, -3, -4, -5)
        rect_dict = r5.to_dictionary()
        self.assertEqual(rect_dict, {
            'id': -5, 'width': -1, 'height': -2, 'x': -3, 'y': -4
        })


if __name__ == '__main__':
    unittest.main()
