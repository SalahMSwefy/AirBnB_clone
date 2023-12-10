#!/usr/bin/python3
"""
Test cases for Amenity class.
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class testAmenity(unittest.TestCase):
    """
    Amenity test class.
    """

    def test_amenity(self):
        """
        Testing instances.
        """
        inst = Amenity()
        self.assertTrue(isinstance(inst, Amenity))
        self.assertTrue(isinstance(inst, BaseModel))
        self.assertTrue(hasattr(inst, 'name'))
        self.assertEqual(inst.name, "")
        inst.name = "test"
        self.assertEqual(inst.name, "test")
        self.assertTrue(isinstance(inst.name, str))
        self.assertTrue(inst.name, "")
        self.assertTrue(inst.id, "")
        self.assertTrue(inst.created_at, "")
        self.assertTrue(inst.updated_at, "")
        self.assertTrue(inst.__class__.__name__, "Amenity")
        self.assertTrue(type(inst.created_at), 'datetime.datetime')
        self.assertTrue(type(inst.updated_at), 'datetime.datetime')
        self.assertTrue(type(inst.id), 'str')
        self.assertTrue(type(inst.name), 'str')
        self.assertTrue(inst.created_at, inst.updated_at)

if __name__ == "__main__":
    unittest.main()
