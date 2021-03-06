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

    #############################
    ## PRE CHECK DOCUMENTATION ##
    #############################

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
        result = pep8style.check_files(["tests/test_models/test_base_model.py"])
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

    ####################
    #### SETUP CLASS ###
    ####################

    def setUpClass(self):
        """
        Creates an instance
        and check if it is
        a class or not.
        """

        base_model = BaseModel()
        
    def test_instantization(self):
        """todo"""

    def tearDownClass(self):
        del self.base_model

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
        self.assertTrue(base_model.created_at, datetime.datetime)

    def test_updated_type(self):
        """
        Test that updated_at
        attribute is datetime object.
        """

        base_model = BaseModel()
        self.assertTrue(base_model.updated_at, datetime.datetime)

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
        rep = "[{}] ({}) <{}>".format(
        self.__class__.__name__, self.id, self.__dict__)

        self.assertEqual(str(base_class), rep)

    def test_save(self):
        """
        Test that `updated_at` atrribute
        datetime is current time.
        """

        base_class = BaseModel()
        

