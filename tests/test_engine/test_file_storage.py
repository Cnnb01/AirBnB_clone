#!/usr/bin/python3
"""Defines unittests for file_storage.py."""
import os
import json
import unittest
from models.base_model import BaseModel
import models
from models.engine.file_storage import FileStorage
from models.user import User


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
        user = User()
        models.storage.new(obj)
        models.storage.new(user)
        all_objects = models.storage.all()
        key_obj = f"{obj.__class__.__name__}{obj.id}"
        key_user = f"{user.__class__.__name__}{user.id}"
        self.assertIn(key_obj, all_objects)
        self.assertIn(key_user, all_objects)
        self.assertIn(key_obj, models.storage.all().keys())
        self.assertIn(key_user, models.storage.all().keys())
        self.assertEqual(all_objects[key_obj], obj.to_dict())
        self.assertEqual(all_objects[key_user], user.to_dict())

    # def test_save(self):
    #     """tests the save method"""
    #     import models
    #     obj = BaseModel()
    #     models.storage.new(obj)
    #     models.storage.save()
    #     self.assertTrue(os.path.exists(models.storage._FileStorage.__file_path))

    def test_save(self):
        basemodel = BaseModel()
        user = User()
        models.storage.new(basemodel)
        models.storage.new(user)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + basemodel.id, save_text)
            self.assertIn("User." + user.id, save_text)

    def test_reload(self):
        """tests the reload method"""
        obj = BaseModel()
        user = User()
        models.storage.new(obj)
        models.storage.new(user)
        models.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        key_obj = f"{obj.__class__.__name__}.{obj.id}"
        key_user = f"{user.__class__.__name__}.{user.id}"
        self.assertIn(key_obj, new_storage.all())
        self.assertIn(key_user, new_storage.all())
        self.assertEqual(new_storage.all()[key_obj], obj.to_dict())
        self.assertEqual(new_storage.all()[key_user], user.to_dict())


if __name__ == '__main__':
    unittest.main()
