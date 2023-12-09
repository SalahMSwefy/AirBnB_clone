#!/usr/bin/python3
"""test cases for FileStorage class"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import json
import pep8


class testFileStorage(unittest.TestCase):
    """CLASS testFileStorage"""
    def test_pep8(self):
        """PEP8 test"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """docstring test"""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.__init__.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_init(self):
        """init test"""
        inst = FileStorage()
        self.assertTrue(isinstance(inst, FileStorage))
        self.assertTrue(isinstance(inst._FileStorage__objects, dict))
        self.assertTrue(isinstance(inst._FileStorage__file_path, str))
        self.assertEqual(inst._FileStorage__file_path, "file.json")
        self.assertTrue(os.path.exists("file.json"))
        self.assertTrue(isinstance(inst._FileStorage__objects, dict))
        self.assertEqual(inst._FileStorage__objects, {})
        self.assertTrue(isinstance(inst._FileStorage__file_path, str))
        self.assertEqual(inst._FileStorage__file_path, "file.json")
        self.assertTrue(os.path.exists("file.json"))
        os.remove("file.json")
        self.assertFalse(os.path.exists("file.json"))

    def test_all(self):
        """all test"""
        inst = FileStorage()
        self.assertEqual(inst.all(), {})
        self.assertTrue(isinstance(inst.all(), dict))
        self.assertTrue(isinstance(inst._FileStorage__objects, dict))
        self.assertEqual(inst._FileStorage__objects, {})
        inst._FileStorage__objects = {"BaseModel.123": "test"}
        self.assertEqual(inst.all(), {"BaseModel.123": "test"})
        self.assertTrue(isinstance(inst.all(), dict))
        self.assertTrue(isinstance(inst.
                                   _FileStorage__objects, dict))
        self.assertEqual(inst._FileStorage__objects, {"BaseModel.123": "test"})
        inst._FileStorage__objects = {"BaseModel.123": "test",
                                      "BaseModel.456": "test2"}
        self.assertEqual(inst.all(), {"BaseModel.123": "test",
                                      "BaseModel.456": "test2"})
        self.assertTrue(isinstance(inst.all(), dict))
        self.assertTrue(isinstance(inst._FileStorage__objects, dict))
        self.assertEqual(inst._FileStorage__objects,
                         {"BaseModel.123": "test", "BaseModel.456": "test2"})

    def test_new(self):
        """new test"""
        inst = FileStorage()
        inst.new("BaseModel.123", "test")
        self.assertEqual(inst.all(), {"BaseModel.123": "test"})
        self.assertTrue(isinstance(inst.all(), dict))
        self.assertTrue(isinstance(inst._FileStorage__objects, dict))
        self.assertEqual(inst._FileStorage__objects, {"BaseModel.123": "test"})
        inst.new("BaseModel.456", "test2")
        self.assertEqual(inst.all(), {"BaseModel.123":
                                      "test", "BaseModel.456": "test2"})
        self.assertTrue(isinstance(inst.all(), dict))
        self.assertTrue(isinstance(inst._FileStorage__objects, dict))
        self.assertEqual(inst._FileStorage__objects,
                         {"BaseModel.123": "test", "BaseModel.456": "test2"})
        inst.new("BaseModel.123", "test3")

    def test_save(self):
        """save test"""
        inst = FileStorage()
        inst.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as f:
            self.assertEqual(json.load(f), {})
        inst.new("BaseModel.123", "test")
        inst.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as f:
            self.assertEqual(json.load(f), {"BaseModel.123": "test"})
        inst.new("BaseModel.456", "test2")
        inst.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as f:
            self.assertEqual(json.load(f), {"BaseModel.123": "test",
                                            "BaseModel.456": "test2"})
        inst.new("BaseModel.123", "test3")
        inst.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as f:
            self.assertEqual(json.load(f), {"BaseModel.123": "test3",
                                            "BaseModel.456": "test2"})
        inst.new("BaseModel.123", "test")
        inst.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """reload test"""
        inst = FileStorage()
        inst.save()
        inst.reload()
        self.assertEqual(inst.all(), {})
        self.assertTrue(isinstance(inst.all(), dict))
        self.assertTrue(isinstance(inst._FileStorage__objects, dict))
        self.assertEqual(inst._FileStorage__objects, {})
        inst.new("BaseModel.123", "test")
        inst.save()
        inst.reload()
        self.assertEqual(inst.all(), {"BaseModel.123": "test"})
        self.assertTrue(isinstance(inst.all(), dict))
        self.assertTrue(isinstance(inst._FileStorage__objects, dict))
        self.assertEqual(inst._FileStorage__objects, {"BaseModel.123": "test"})
        inst.new("BaseModel.456", "test2")
        inst.save()
        inst.reload()
        self.assertEqual(inst.all(),
                         {"BaseModel.123": "test", "BaseModel.456": "test2"})
        self.assertTrue(isinstance(inst.all(), dict))
        self.assertTrue(isinstance(inst._FileStorage__objects, dict))
        self.assertEqual(inst._FileStorage__objects,
                         {"BaseModel.123": "test", "BaseModel.456": "test2"})
        inst.new("BaseModel.123", "test3")
        inst.save()
        inst.reload()
        self.assertEqual(inst.all(),
                         {"BaseModel.123": "test3", "BaseModel.456": "test2"})
        self.assertTrue(isinstance(inst.all(), dict))
        self.assertTrue(isinstance(inst._FileStorage__objects, dict))
        self.assertEqual(inst._FileStorage__objects,
                         {"BaseModel.123": "test3", "BaseModel.456": "test2"})
        inst.new("BaseModel.123", "test")
        inst.save()
        inst.reload()
        self.assertEqual(inst.all(),
                         {"BaseModel.123": "test", "BaseModel.456": "test2"})
        self.assertTrue(isinstance(inst.all(), dict))
        self.assertTrue(isinstance(inst._FileStorage__objects, dict))
        self.assertEqual(inst._FileStorage__objects,
                         {"BaseModel.123": "test", "BaseModel.456": "test2"})
        inst.new("BaseModel.123", "test")
        inst.save()
        inst.reload()
        self.assertEqual(inst.all(),
                         {"BaseModel.123": "test", "BaseModel.456": "test2"})
        self.assertTrue(isinstance(inst.all(), dict))
        self.assertTrue(isinstance(inst._FileStorage__objects, dict))
