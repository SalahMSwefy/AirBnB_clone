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
        