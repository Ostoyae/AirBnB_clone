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

            self.__objects.update({key: base})

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

            try:
                with open(self.__file_path, encoding="utf-8") as fp:
                    self.__objects = json.JSONDecoder().decode(fp.read())

            except Exception:
                self.__objects = {}
