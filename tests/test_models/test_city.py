#!/usr/bin/python3
"""CITY MODULE TESTS"""
import unittest
import models
import os
from datetime import datetime
from models.city import City


class TestCityModel(unittest.TestCase):
    """TASK 10 UNIT TESTS"""
    def test_init(self):
        self.assertEqual(City, type(City()))

    def test_sta_id(self):
        tulsa = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(tulsa))
        self.assertNotIn("state_id", tulsa.__dict__)

if __name__ == "__main__":
    unittest.main()
