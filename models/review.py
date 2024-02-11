#!/usr/bin/python3
"""Contains class review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Child class of BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
