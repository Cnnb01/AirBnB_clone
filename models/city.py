#!/usr/bin/python3
"""Defines the user class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Child class of BaseModel"""

    state_id = ""
    name = ""
