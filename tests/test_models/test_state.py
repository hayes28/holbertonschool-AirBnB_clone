#!/usr/bin/python3
"""STATE MODULE TESTS"""
import unittest
import models
import os
from datetime import datetime
from models.state import State


class TestStateModel(unittest.TestCase):
    """TASK 10 UNIT TESTS"""
    def test_init(self):
        self.assertEqual(State, type(State()))

    def test_state_name(self):
        ok = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(State()))
        self.assertNotIn("name", ok.__dict__)

if __name__ == "__main__":
    unittest.main()
