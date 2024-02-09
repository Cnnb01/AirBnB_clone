#!/usr/bin/python3
import json
import os
from base_model import BaseModel


class FileStorage:
    def __init__(self, __file_path):
        self.__file_path = __file_path
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj.to_dict

    def save(self):
        with open(self.__objects, 'w') as file:
            json.dump(self.__objects, file)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
