#!/usr/bin/python3
import uuid
from datetime import datetime
from models.__init__ import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.kwargs = kwargs
        if not kwargs:
            storage.new(self)

    def __str__(self):
        return f"{self.__class__.__name__} {self.id}"

    def save(self):
        self.updated_at = datetime.now()
        storage.save()
        return self.updated_at

    def to_dict(self):
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()

        if self.kwargs:
            for k, v in self.kwargs.items():
                setattr(self, k, v)
        self.created_at = datetime.fromisoformat(self.created_at)
        self.updated_at = datetime.fromisoformat(self.updated_at)
        return self.__dict__
