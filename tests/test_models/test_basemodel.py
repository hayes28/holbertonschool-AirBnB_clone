import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_bas_mod_id(self):
        bm1 = BaseModel()
        self.assertIsInstance(bm1.id, str)

    def test_bas_mod_crt(self):
        bm1 = BaseModel()
        self.assertIsInstance(bm1.created_at, datetime)

    def test_bas_mod_upd(self):
        bm1 = BaseModel()
        self.assertIsInstance(bm1.updated_at, datetime)

    def test_uwu_id(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_ini_tim(self):
        bm1 = BaseModel()
        self.assertEqual(bm1.created_at, bm1.updated_at)

    def test_sav_upd_met(self):
        bm1 = BaseModel()
        cat = bm1.created_at
        uat = bm1.updated_at
        bm1.save()
        self.assertEqual(bm1.created_at, cat)
        self.assertNotEqual(bm1.updated_at, uat)

    def test_richard(self):
        bm1 = BaseModel()
        richard = bm1.to_dict()
        self.assertIsInstance(richard, dict)

if __name__ == "__main__":
    unittest.main()
