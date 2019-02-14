#!/usr/bin/python3
"""
Test for BaseModel
"""
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        del self.base_model

    def test_type(self):
        self.assertTrue(isinstance(self.base_model, BaseModel))  # pointless but simple test

    def test_id(self):
        other = BaseModel()
        self.assertNotEqual(self.base_model.id, other.id)  # first check if different objects

    def test_to_dict(self):
        self.assertTrue(isinstance(self.base_model.to_dict(), dict))

    def test_kwargs(self):
        other = BaseModel(id="42", name="Hello Kitty")
        self.assertEqual(other.id, "42")
        self.assertEqual(other.name, "Hello Kitty")

    def test_from_dict(self):
        other = BaseModel(**self.base_model.to_dict())
        self.assertEqual(self.base_model.to_dict(), other.to_dict())  # compare dictionaries

    def test_str(self):
        d = {'created_at': '2019-02-14T03:52:04.684419', 'updated_at': '2019-02-14T03:52:04.684419',
             'id': '58830545-4cca-4cb8-a2f8-883b02efe7df', '__class__': 'BaseModel'}
        s = "[BaseModel] (58830545-4cca-4cb8-a2f8-883b02efe7df) {'created_at': datetime.datetime(2019, 2, 14, 3, 52, 4, 684419), 'updated_at': datetime.datetime(2019, 2, 14, 3, 52, 4, 684419), 'id': '58830545-4cca-4cb8-a2f8-883b02efe7df'}"
        other = BaseModel(**d)
        self.assertEqual(str(other), s)
