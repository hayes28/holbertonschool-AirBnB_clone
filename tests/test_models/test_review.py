#!/usr/bin/python3
"""REVIEW MODULE TESTS"""
import unittest
import models
import os
from datetime import datetime
from models.review import Review


class TestReviewModel(unittest.TestCase):
    """TASK 10 UNIT TESTS"""
    def test_init(self):
        self.assertEqual(Review, type(Review()))

    def test_review_pid(self):
        villager_noise = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(Review()))
        self.assertNotIn("place_id", villager_noise.__dict__)

    def test_review_uid(self):
        villager_noise = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(Review()))
        self.assertNotIn("user_id", villager_noise.__dict__)

if __name__ == "__main__":
    unittest.main()
