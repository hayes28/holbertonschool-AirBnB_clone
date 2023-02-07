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

if __name__ == "__main__":
    unittest.main()
