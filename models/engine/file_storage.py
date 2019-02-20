#!/usr/bin/python3
"""
FileStorage class is the backbone
of the file storage engine.
"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


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

        return self.__objects

    def new(self, obj):
        """Method that writes classname.id to dictionary.

        Args:
            obj: Object class to serialize to json.
        """

        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            base = obj.to_dict()

            if obj.__class__.__name__ is not 'BaseModel':

                pub_cls = {
                    k: v
                    for k, v in obj.__class__.__dict__.items()
                    if '__' not in k
                }

                base.update(pub_cls)
                obj = obj.__class__(**base)

            self.__objects.update({key: obj})

    def save(self):
        """Serializes `__objects` to JSON file path"""

        to_save = {}

        with open(self.__file_path, "w", encoding="utf-8") as fp:
            for key, value in self.__objects.items():
                to_save[key] = value.to_dict()

            json.dump(to_save, fp)

    def reload(self):
        """
        Deserializes JSON file to
        `__objects` conditional on
        existence of file path.
        """

        try:
            with open(self.__file_path, encoding="utf-8") as fp:

                file_handle = json.load(fp)
                for key, value in file_handle.items():
                    self.__objects[key] = globals()[
                                    value['__class__']
                                    ](**value)

        except Exception:
            self.__objects = {}
