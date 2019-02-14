#!/usr/bin/python3
"""
Defines BaseModel class
"""

import uuid
import models
import datetime


class BaseModel():
    """Base class that other models/classes derive from"""

    def __init__(self, *args, **kwargs):
        """Instantiates the base model.

        Args:
            args: non-keyworded arguments to method(s)
            kwargs: keyworded arguments to method(s)

        Raises:
            none

        Returns:
            none
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Returns string repr. of `BaseClass` model."""

        return "[{}] ({}) <{}>".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates `updated_at` attribute."""

        self.updated_at = self.created_at

    def to_dict(self):
        """Converts time attributes to ISO 8601 format."""

        attrs = self.__dict__.copy()

        for k, v in self.__dict__.items():

            if k == "created_at":
                attrs["created_at"] = attrs["created_at"].isoformat()

            elif k == "updated_at":
                attrs["updated_at"] = attrs["updated_at"].isoformat()

        atts["__class__"] = self.__class__.__name__
        return attrs
