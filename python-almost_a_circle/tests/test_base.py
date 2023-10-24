#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_base_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_base_id_increment(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_base_id_custom(self):
        b3 = Base(100)
        self.assertEqual(b3.id, 100)

    def test_get_nb_objects(self):
        self.assertEqual(Base.get_nb_objects(), 3)


if __name__ == '__main__':
    unittest.main()
