#!/usr/bin/python3
"""test cases for Place class"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class testPlace(unittest.TestCase):
    """Place test class"""

    def test_place(self):
        """Testing instances"""
        inst = Place()
        self.assertTrue(isinstance(inst, Place))
        self.assertTrue(isinstance(inst, BaseModel))
        self.assertTrue(hasattr(inst, 'city_id'))
        self.assertTrue(hasattr(inst, 'user_id'))
        self.assertTrue(hasattr(inst, 'name'))
        self.assertTrue(hasattr(inst, 'description'))
        self.assertTrue(hasattr(inst, 'number_rooms'))
        self.assertTrue(hasattr(inst, 'number_bathrooms'))
        self.assertTrue(hasattr(inst, 'max_guest'))
        self.assertTrue(hasattr(inst, 'price_by_night'))
        self.assertTrue(hasattr(inst, 'latitude'))
        self.assertTrue(hasattr(inst, 'longitude'))
        self.assertTrue(hasattr(inst, 'amenity_ids'))
        self.assertEqual(inst.city_id, "")
        self.assertEqual(inst.user_id, "")
        self.assertEqual(inst.name, "")
        self.assertEqual(inst.description, "")
        self.assertEqual(inst.number_rooms, 0)
        self.assertEqual(inst.number_bathrooms, 0)
        self.assertEqual(inst.max_guest, 0)
        self.assertEqual(inst.price_by_night, 0)
        self.assertEqual(inst.latitude, 0.0)
        self.assertEqual(inst.longitude, 0.0)
        self.assertEqual(inst.amenity_ids, [])
        inst.city_id = "123"
        self.assertEqual(inst.city_id, "123")
        self.assertTrue(isinstance(inst.city_id, str))
        inst.user_id = "123"
        self.assertEqual(inst.user_id, "123")
        self.assertTrue(isinstance(inst.user_id, str))
        inst.name = "test"
        self.assertEqual(inst.name, "test")
        self.assertTrue(isinstance(inst.name, str))
        inst.description = "test"
        self.assertEqual(inst.description, "test")
        self.assertTrue(isinstance(inst.description, str))
        inst.number_rooms = 1
        self.assertEqual(inst.number_rooms, 1)
        self.assertTrue(isinstance(inst.number_rooms, int))
        inst.number_bathrooms = 1
        self.assertEqual(inst.number_bathrooms, 1)
        self.assertTrue(isinstance(inst.number_bathrooms, int))
        inst.max_guest = 1
        self.assertEqual(inst.max_guest, 1)
        self.assertTrue(isinstance(inst.max_guest, int))
        inst.price_by_night = 1
        self.assertEqual(inst.price_by_night, 1)
        self.assertTrue(isinstance(inst.price_by_night, int))
        inst.latitude = 1.0
        self.assertEqual(inst.latitude, 1.0)
        self.assertTrue(isinstance(inst.latitude, float))
        inst.longitude = 1.0
        self.assertEqual(inst.longitude, 1.0)
        self.assertTrue(isinstance(inst.longitude, float))
        inst.amenity_ids = ["123"]
        self.assertEqual(inst.amenity_ids, ["123"])
        self.assertTrue(isinstance(inst.amenity_ids, list))

if __name__ == "__main__":
    unittest.main()
