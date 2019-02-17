#!/usr/bin/python3
"""
Creates module that contains unique
instance of FileStorage.
"""


from models.engine import FileStorage

storage = FileStorage()
storage.reload()
