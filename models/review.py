#!/usr/bin/python3
""" Modules for Review Class
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """Class for Review Object
    Inherts from BaseModel
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self):
        pass
