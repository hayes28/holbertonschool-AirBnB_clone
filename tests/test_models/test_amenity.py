#!/usr/bin/python3
"""AMENITY MODULE TESTS"""
import unittest
import models
import os
from datetime import datetime
from models.amenity import Amenity


class TestAmenityModel(unittest.TestCase):
    """TASK 10 UNIT TESTS"""
    def test_init(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_name_pub(self):
        pool = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", pool.__dict__)

if __name__ == "__main__":
    unittest.main()
