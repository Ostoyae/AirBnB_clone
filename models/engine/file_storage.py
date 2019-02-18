#!/usr/bin/python3
"""
FileStorage class is the backbone
of the file storage engine.
"""
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

        return self.__objects

    def new(self, obj):
        """Method that writes classname.id to dictionary."""

        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj.to_dict()

    def save(self):
        """Serializes `__objects` to JSON file path"""

        to_save = {}

        with open(self.__file_path, "w", encoding="utf-8") as fp:
            for key, value in self.__objects.items():
                to_save[key] = value

            json.dump(to_save, fp)

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
