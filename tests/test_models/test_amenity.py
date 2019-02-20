#!/usr/bin/python3
"""
Test module for Amenity class.
"""

import os
import pep8
import unittest
from models.amenity import Amenity
from models import storage


class TestAmenity(unittest.TestCase):
    """
    Unittest for
    Amenity class.
    """

    amenity = Amenity()
    o_id = '{}.{}'.format('Amenity', amenity.id)

    def setUp(self):
        self.objects = storage.all()

    def tearDown(self):
        pass

    def test_style_check(self):
        pep8style = pep8.StyleGuide(quiet=True)
        p = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_attr(self):
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)

    def test_documentation(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_class(self):
        self.assertTrue(isinstance(self.amenity, Amenity))

    def test_id(self):
        self.assertTrue(type(self.amenity.id), int)

    def test_name(self):
        self.assertTrue(type(self.amenity.name), str)

    def test_field_name(self):
        d = self.objects[self.o_id]
        self.assertTrue(any(k == 'name' for k in d.keys()))

    def test_update(self):
        cur_time = self.objects[self.o_id]['updated_at']
        self.amenity.save()
        new_time = self.amenity.to_dict()['updated_at']
        self.assertNotEqual(cur_time, new_time)

    def test_load_from_dict(self):
        new = Amenity(**self.objects[self.o_id])
        self.assertEqual(new.to_dict(), self.objects[self.o_id])

    def test_no_private_attrs(self):
        for k in self.objects[self.o_id].keys():
            if k is not '__class__':
                self.assertTrue(('__' not in k))

    def test_class_attr(self):
        self.assertEqual(self.objects[self.o_id]['__class__'], 'Amenity')
