#!/usr/bin/python3
""" Modules for City Class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class for City Object
    Inherts from BaseModel
    """

    state_id = ""
    name = ""
