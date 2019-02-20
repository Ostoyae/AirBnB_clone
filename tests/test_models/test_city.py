#!/usr/bin/python3
"""
Test module for City class
"""

import os
import pep8
import unittest
from models.city import City
from models import storage


class TestCity(unittest.TestCase):
    """
    Unittest for City class.
    """

    city = City()
    o_id = '{}.{}'.format('City', city.id)

    def setUp(self):
        self.objects = storage.all()

    def tearDown(self):
        try:
            os.remove("file.json")

        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        check for pep8 compliant
        """

        pep8style = pep8.StyleGuide(quiet=True)
        p = pep8style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_attr(self):
        """
        test for BaseModel attrs
        """

        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)

    def test_documentation(self):
        """
        test for docs
        """

        self.assertIsNotNone(City.__doc__)

    def test_class(self):
        """
        test if a class was instance correctly
        """

        self.assertTrue(isinstance(self.city, City))

    def test_id(self):
        """
        test class id
        """

        self.assertTrue(type(self.city.id), int)

    def test_name(self):
        """
        Test pub class attr name was impl
        """

        self.assertTrue(type(self.city.name), str)

    def test_name(self):
        """
        Test pub class attr name was impl
        """

        d = self.objects[self.o_id].to_dict()
        self.assertTrue(any(k == 'name' for k in d))

    def test_field_state_id(self):
        """
        Test pub class attr state_id was impl
        """

        d = self.objects[self.o_id].to_dict()
        self.assertTrue(any(k == 'state_id' for k in d.keys()))

    def test_update(self):
        """
        test updating updated_at
        """

        cur_time = self.objects[self.o_id].to_dict()['updated_at']
        self.city.save()
        new_time = self.city.to_dict()['updated_at']
        self.assertNotEqual(cur_time, new_time)

    def test_load_from_dict(self):
        """
        test load User from dictionary
        """

        new = City(**self.objects[self.o_id].to_dict())
        self.assertEqual(new.to_dict(), self.objects[self.o_id])

    def test_no_private_attrs(self):
        """
        test that no private class var were added from User
        """

        for k in self.objects[self.o_id].to_dict():
            if k is not '__class__':
                self.assertTrue(('__' not in k))

    def test_class_attr(self):
        """
        Test storaged object is class User
        """

        self.assertEqual(self.objects[self.o_id].to_dict()[
            '__class__'], 'City')
