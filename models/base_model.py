#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        # self.kwargs = kwargs
    
    def __str__(self):
        return f"{self.__class__.__name__} {self.id}"
    
    def save(self):
        self.updated_at = datetime.now()
        return self.updated_at 
    
    def to_dict(self):
        # if kwargs:
        #     for k in kwargs.iteritems():

        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return self.__dict__ 