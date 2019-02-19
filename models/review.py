#!/usr/bin/python3
""" Modules for Review Class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Defines public attribute for class Review
    """

    place_id = ""
    user_id = ""
    text = ""
