#!/usr/bin/python3
"""__init__ file for models directory"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.city import City

classes = {"BaseModel": BaseModel,
           "User": User,
           "Place": Place,
           "State": State,
           "Review": Review,
           "Amenity": Amenity,
           "City": City}

storage = FileStorage()
storage.reload()
