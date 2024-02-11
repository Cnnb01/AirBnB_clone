#!/usr/bin/python3
"""Defines the user class"""

from models.base_model import BaseModel


class User(BaseModel):
    """Child class of BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialize User instance"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
