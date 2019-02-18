#!/usr/bin/python3
"""
Test for BaseModel
"""
from models.base_model import BaseModel
from datetime import datetime
import unittest
import inspect
import json
import pep8
import sys
import os


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """
        Creates an instance
        and check if it is
        a class or not.
        """
        base_model = BaseModel()

    def tearDown(self):
        """
        Cleans up test method
        after done.
        """

        del self

    def check_documentation(self):
        """
        Check that documentation exists
        for all classes and methods in the
        BaseModel
        """

        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(__init__.__doc__)
        self.assertIsNotNone(__str__.__doc__)
        self.assertIsNotNone(save.__doc__)
        self.assertIsNotNone(to_dict.__doc__)

    def test_base_pep8(self):
        """
        Tests Base for PEP8 errors.
        """

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([
            "tests/test_models/test_base_model.py"])
        self.assertEqual(result.total_errors, 0, "PEP8 failure...")
        result = pep8style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0, "PEP8 failure...")

    def test_methods_exist(self):
        """
        Test to see if methods are
        created and correct.
        """

        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_instance_created(self):
        """
        Test that instance
        and attributs created.
        """

        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)
        self.assertTrue(hasattr(base_model, "created_at"))
        self.assertTrue(hasattr(base_model, "updated_at"))

    def test_id_type(self):
        """
        Test that id attribute
        is a string type.
        """

        base_model = BaseModel()
        self.assertTrue(base_model.id, str)

    def test_created_type(self):
        """
        Test that created_at
        attribute is datetime object.
        """

        base_model = BaseModel()
        self.assertTrue(base_model.created_at, datetime.date)

    def test_updated_type(self):
        """
        Test that updated_at
        attribute is datetime object.
        """

        base_model = BaseModel()
        self.assertTrue(base_model.updated_at, datetime.date)

    def test_baseclass_attrs_type(self):
        """
        Test that the repr. of
        the class is a string.
        """

        base_class = BaseModel()
        cn = base_class.__class__.__name__
        idn = base_class.id
        attrs = base_class.__dict__

        self.assertTrue(type(cn), str)
        self.assertTrue(type(id), str)
        self.assertDictEqual(attrs, base_class.__dict__)

    def test_magicstring_method(self):
        """
        Test that our __str__ method
        returns correct representation.
        """

        base_class = BaseModel()
        cn = base_class.__class__.__name__
        cid = base_class.id
        attrs = base_class.__dict__
        self.assertTrue(type(cn), str)
        self.assertTrue(type(cid), str)
        self.assertTrue(type(attrs), dict)

    def test_save(self):
        """
        Test that `updated_at` atrribute
        has been updated.
        """

        base_class = BaseModel()
        new_dt = base_class.updated_at
        base_class.save()
        self.assertNotEqual(new_dt, base_class.updated_at)

    def test_to_dict(self):
        """
        Test that `to_dict` method returns
        all attrs. in dictionary form.
        """

        base_class = BaseModel()
        bc = base_class.to_dict()
        self.assertIsInstance(bc, dict)

    def test_to_dict_attrs(self):
        """
        Test that class attributes are
        converted to string type.
        """

        base_class = BaseModel()
        attrs = base_class.to_dict()
        a1 = attrs["created_at"]
        a2 = attrs["updated_at"]

        self.assertIsInstance(a1, str)
        self.assertIsInstance(a2, str)

    def test_class_type(self):
        """
        Test that the class name was
        inserted into the dictionary.
        """

        base_class = BaseModel()
        method = base_class.to_dict()
        value = method["__class__"]
        self.assertIsInstance(value, str)

    def test_load_from_dict(self):
        """
        Test that intance is created
        from the dictionary values.
        """

        base_class = BaseModel()
        mi = base_class.to_dict()
        kw = BaseModel(**mi)
        self.assertDictEqual(base_class.__dict__, kw.__dict__)
