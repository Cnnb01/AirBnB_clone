#!/usr/bin/python3
"""
This module defines the FileStorage class.

FileStorage:
    Represents a simple file storage system for serializing
    and deserializing instances.

Attributes:
    __file_path (str): The path to the JSON file used for storage.
    __objects (dict): A dictionary storing instances in the
    format {class_name.id: instance_dict}.

Methods:
    all: Returns the dictionary of all stored objects.
    new: Adds a new object to the storage dictionary.
    save: Serializes the storage dictionary to the JSON file.
    reload: Deserializes the JSON file to populate the storage dictionary.

"""


import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    The FileStorage class represents a simple file storage
    system for serializing and deserializing instances.

    Attributes:
        __file_path (str): The path to the JSON file used for storage.
        __objects (dict): A dictionary storing instances in
        the format {class_name.id: instance_dict}.

    Methods:
        all: Returns the dictionary of all stored objects.
        new: Adds a new object to the storage dictionary.
        save: Serializes the storage dictionary to the JSON file.
        reload: Deserializes the JSON file to populate the storage dictionary.

    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all stored objects.

        Returns:
            dict: A dictionary containing instances
            in the format {class_name.id: instance_dict}.

        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.

        Args:
            obj: The instance to be added to the storage.

        """
        key = "{}{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """
        Serializes the storage dictionary to the JSON file.

        """
        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file)

    def reload(self):
        """
        Deserializes the JSON file to populate the storage dictionary.

        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                try:
                    self.__objects = json.load(file)
                except FileNotFoundError:
                    pass
