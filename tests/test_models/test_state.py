#!/usr/bin/python3
"""test cases for State class"""
import unittest
from models.state import State
from models.base_model import BaseModel


class testState(unittest.TestCase):
    """State test class"""

    def test_state(self):
        """Testing instances"""
        inst = State()
        self.assertTrue(isinstance(inst, State))
        self.assertTrue(isinstance(inst, BaseModel))
        self.assertTrue(hasattr(inst, 'name'))
        self.assertEqual(inst.name, "")
        inst.name = "test"
        self.assertEqual(inst.name, "test")
        self.assertTrue(isinstance(inst.name, str))

if __name__ == "__main__":
    unittest.main()
