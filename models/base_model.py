#!/usr/bin/python3
import uuid
from datetime import datetime
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        if not kwargs:#if no key words, a new instance is created
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:#if there are key words, it sets the attributes based on the provided kw, then if the dates are provided they are converted to objects
            for k, v in kwargs.items():
                setattr(self, k, v)
            if 'created_at' in kwargs:
                self.created_at = datetime.fromisoformat(self.created_at)
            if 'updated_at' in kwargs:
                self.updated_at = datetime.fromisoformat(self.updated_at)

    def __str__(self):
        return f"{self.__class__.__name__} {self.id}"

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()
        return self.updated_at

    def to_dict(self):
        dict_copy = self.__dict__.copy()
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy

