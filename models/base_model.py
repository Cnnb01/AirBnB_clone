#!/usr/bin/python3
"""
This module defines the BaseModel class.

BaseModel:
    Represents the base model for other classes.
"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """
    The BaseModel class represents the base model for other classes.

    Attributes:
        id (str): The unique identifier for each instance.
        created_at (datetime): The timestamp when the instance is created.
        updated_at (datetime): The timestamp when the instance is updated.

    Methods:
        __init__: Initializes a new instance of the BaseModel class.
        __str__: Returns a string representation of the instance.
        save: Updates the instance's 'updated_at' attribute
        and saves the changes.
        to_dict: Converts the instance to a dictionary.

    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        If no keyword arguments are provided, a new instance is created with
        a unique identifier, creation timestamp, and update
        timestamp. If keyword arguments are provided, it sets the
        attributes based on the provided keywords.
        If 'created_at' and 'updated_at' are provided,
        they are converted to datetime
        objects.

        Args:
            args: Non-keyword arguments (not used).
            kwargs: Keyword arguments for setting instance attributes.

        """
        if not kwargs:
            # if no key words, a new instance is created
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            # if there are key words, it sets the attributes based
            # on the provided kw, then if the dates are provided convert 2 objs
            for k, v in kwargs.items():
                setattr(self, k, v)
            if 'created_at' in kwargs and 'updated_at' in kwargs:
                self.created_at = datetime.fromisoformat(kwargs['created_at'])
                self.updated_at = datetime.fromisoformat(kwargs['updated_at'])

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: A string representation of the instance.

        """
        return f"{self.__class__.__name__} {self.id}"

    def save(self):
        """
        Updates the instance's 'updated_at' attribute and saves the changes.

        Returns:
            datetime: The updated 'updated_at' timestamp.

        """
        self.updated_at = datetime.now()
        models.storage.save()
        return self.updated_at

    def to_dict(self):
        """
        Converts the instance to a dictionary.

        Returns:
            dict: A dictionary representation of the instance.

        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
