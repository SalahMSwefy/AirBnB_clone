#!/usr/bin/python3
"""test cases for User class"""
import unittest
from models.user import User
from models.base_model import BaseModel


class testUser(unittest.TestCase):
    """User test class"""

    def test_user(self):
        """Testing instances"""
        inst = User()
        self.assertTrue(isinstance(inst, User))
        self.assertTrue(isinstance(inst, BaseModel))
        self.assertTrue(hasattr(inst, 'email'))
        self.assertTrue(hasattr(inst, 'password'))
        self.assertTrue(hasattr(inst, 'first_name'))
        self.assertTrue(hasattr(inst, 'last_name'))
        self.assertEqual(inst.email, "")
        self.assertEqual(inst.password, "")
        self.assertEqual(inst.first_name, "")
        self.assertEqual(inst.last_name, "")
        inst.email = "test"
        self.assertEqual(inst.email, "test")
        self.assertTrue(isinstance(inst.email, str))
        inst.password = "test"
        self.assertEqual(inst.password, "test")
        self.assertTrue(isinstance(inst.password, str))
        inst.first_name = "test"
        self.assertEqual(inst.first_name, "test")
        self.assertTrue(isinstance(inst.first_name, str))
        inst.last_name = "test"
        self.assertEqual(inst.last_name, "test")
        self.assertTrue(isinstance(inst.last_name, str))

if __name__ == "__main__":
    unittest.main()
