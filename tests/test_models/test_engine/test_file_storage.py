#!/usr/bin/python3
"""Thomas Unit Test Module"""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """file storage uwunit tests"""
