#!/usr/bin/python3
"""Defines unittests for file_storage.py."""
import os
import json
import unittest
from models.base_model import BaseModel
import models
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_all(self):
        """tests the all method"""
        models.storage = FileStorage()
        all_objects = models.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(all_objects, {})

    def test_new(self):
        """tests the new method"""
        models.storage = FileStorage()
        obj = BaseModel()
        models.storage.new(obj)
        all_objects = models.storage.all()
        key = f"{obj.__class__.__name__}{obj.id}"
        self.assertIn(key, all_objects)
        self.assertEqual(all_objects[key], obj.to_dict())

    # def test_save(self):
    #     """tests the save method"""
    #     import models
    #     obj = BaseModel()
    #     models.storage.new(obj)
    #     models.storage.save()
    #     self.assertTrue(os.path.exists(models.storage._FileStorage.__file_path))

    def test_save(self):
        basemodel = BaseModel()
        models.storage.new(basemodel)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + basemodel.id, save_text)

    def test_reload(self):
        """tests the reload method"""
        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        all_objects = new_storage.all()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, all_objects)
        self.assertEqual(all_objects[key], obj.to_dict())


if __name__ == '__main__':
    unittest.main()
