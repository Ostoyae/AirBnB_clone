#!/usr/bin/python3
"""
Defines a User Class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines public attribute for class User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
