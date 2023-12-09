#!/usr/bin/python3
"""test cases for Review class"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class testReview(unittest.TestCase):
    """Review test class"""

    def test_review(self):
        """Testing instances"""
        inst = Review()
        self.assertTrue(isinstance(inst, Review))
        self.assertTrue(isinstance(inst, BaseModel))
        self.assertTrue(hasattr(inst, 'place_id'))
        self.assertTrue(hasattr(inst, 'user_id'))
        self.assertTrue(hasattr(inst, 'text'))
        self.assertEqual(inst.place_id, "")
        self.assertEqual(inst.user_id, "")
        self.assertEqual(inst.text, "")
        inst.place_id = "123"
        self.assertEqual(inst.place_id, "123")
        self.assertTrue(isinstance(inst.place_id, str))
        inst.user_id = "123"
        self.assertEqual(inst.user_id, "123")
        self.assertTrue(isinstance(inst.user_id, str))
        inst.text = "test"
        self.assertEqual(inst.text, "test")
        self.assertTrue(isinstance(inst.text, str))