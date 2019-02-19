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

    def test_field_amenity_ids(self):
        d = self.objects[self.o_id]
        self.assertTrue(any(k == 'amenity_ids' for k in d.keys()))

    def test_update(self):
        cur_time = self.objects[self.o_id]['updated_at']
        self.place.save()
        new_time = self.place.to_dict()['updated_at']
        self.assertNotEqual(cur_time, new_time)
