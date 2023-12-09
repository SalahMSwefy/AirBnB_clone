#!/usr/bin/python3
"""test cases for City class"""
import unittest
from models.city import City
from models.base_model import BaseModel


class testCity(unittest.TestCase):
    """City test class"""

    def test_city(self):
        """Testing instances"""
        inst = City()
        self.assertTrue(isinstance(inst, City))
        self.assertTrue(isinstance(inst, BaseModel))
        self.assertTrue(hasattr(inst, 'name'))
        self.assertTrue(hasattr(inst, 'state_id'))
        self.assertEqual(inst.name, "")
        self.assertEqual(inst.state_id, "")
        inst.name = "test"
        self.assertEqual(inst.name, "test")
        self.assertTrue(isinstance(inst.name, str))
        inst.state_id = "123"
        self.assertEqual(inst.state_id, "123")
        self.assertTrue(isinstance(inst.state_id, str))
