#!/usr/bin/python3
"""
FileStorage class is the backbone
of the file storage engine.
"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.reviews import Reviews
from models.state import State
import json


class FileStorage():
    """
    Engine for file storage system
    to be later used by RDBMS, API,
    and web framework systems.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns `objects` class attr."""

        return __objects

    def new(self, obj):
        """Method that writes classname.id to dictionary."""

        if obj is not None:
            key = self.__class__.__name__ + "." + obj.id
            __objects[key] = obj

    def save(self):
        """Serializes `__objects` to JSON file path"""

        to_save = {}

        with open(self.__file_path, "w", encoding="utf-8") as f:
            for key, value in self.__objects.items():
                to_save[key] = value.to_dict()

            json.dump(to_save, f)

    def reload(self):
        """
        Deserializes JSON file to
        `__objects` conditional on
        existence of file path.
        """

        with open(self.__file_path, encoding="utf-8") as fp:
            try:
                self.__objects = json.JSONDecoder().decode(fp.read())

            except Exception:
                self.__objects = {}
