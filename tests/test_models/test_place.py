#!/usr/bin/python3
"""PLACE MODULE TESTS"""
import unittest
import models
import os
from datetime import datetime
from models.place import Place


class TestPlaceModel(unittest.TestCase):
    """TASK 10 UNIT TESTS"""
    def test_init(self):
        self.assertEqual(Place, type(Place()))

    def test_cid(self):
        aaru = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(aaru))
        self.assertNotIn("city_id", aaru.__dict__)

    def test_uid(self):
        aaru = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(aaru))
        self.assertNotIn("user_id", aaru.__dict__)

if __name__ == "__main__":
    unittest.main()
