#!/usr/bin/python3
"""Test module for Place class
"""

import unittest
import os
from models.place import Place
from models import storage


class TestPlace(unittest.TestCase):

    place = Place()
    o_id = '{}.{}'.format('Place', place.id)

    def setUp(self):
        self.objects = storage.all()

    def tearDown(self):
        try:
            os.remove("file.json")

        except FileNotFoundError:
            pass

    def test_style_check(self):
        pep8style = pep8.StyleGuide(quiet=True)
        p = pep8style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_attr(self):
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)

    def test_documentation(self):
        self.assertIsNotNone(Place.__doc__)

    def test_class(self):
        self.assertTrue(isinstance(self.place, Place))

    def test_id(self):
        self.assertTrue(type(self.place.id), int)

    def test_name(self):
        self.assertTrue(type(self.place.name), str)

    def test_class(self):
        self.assertTrue(isinstance(self.place, Place))

    def test_field_city_id(self):
        d = self.objects[self.o_id]
        self.assertTrue(any(k == 'city_id' for k in d.keys()))

    def test_field_user_id(self):
        d = self.objects[self.o_id]
        self.assertTrue(any(k == 'user_id' for k in d.keys()))

    def test_field_name(self):
        d = self.objects[self.o_id]
        self.assertTrue(any(k == 'name' for k in d.keys()))

    def test_field_description(self):
        d = self.objects[self.o_id]
        self.assertTrue(any(k == 'description' for k in d.keys()))

    def test_number_rooms(self):
        d = self.objects[self.o_id]
        self.assertTrue(any(k == 'number_rooms' for k in d.keys()))

    def test_number_bathrooms(self):
        d = self.objects[self.o_id]
        self.assertTrue(any(k == 'number_bathrooms' for k in d.keys()))

    def test_field_max_guest(self):
        d = self.objects[self.o_id]
        self.assertTrue(any(k == 'max_guest' for k in d.keys()))

    def test_field_price_by_night(self):
        d = self.objects[self.o_id]
        self.assertTrue(any(k == 'price_by_night' for k in d.keys()))

    def test_field_latitude(self):
        d = self.objects[self.o_id]
        self.assertTrue(any(k == 'latitude' for k in d.keys()))

    def test_field_longitude(self):
        d = self.objects[self.o_id]
        self.assertTrue(any(k == 'longitude' for k in d.keys()))

    def test_field_place_ids(self):
        d = self.objects[self.o_id]
        self.assertTrue(any(k == 'place_ids' for k in d.keys()))

    def test_update(self):
        cur_time = self.objects[self.o_id]['updated_at']
        self.place.save()
        new_time = self.place.to_dict()['updated_at']
        self.assertNotEqual(cur_time, new_time)

    def test_load_from_dict(self):
        new = User(**self.objects[self.o_id])
        self.assertEqual(new.to_dict(), self.objects[self.o_id])

    def test_no_private_attrs(self):
        for k in self.objects[self.o_id].keys():
            if k is not '__class__':
                self.assertTrue(('__' not in k))

    def test_class_attr(self):
        self.assertEqual(self.objects[self.o_id]['__class__'], 'Place')
