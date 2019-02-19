#!/usr/bin/python3
"""Test module for User class
"""

import unittest
import os
from models.user import User
from models import storage


class TestUser(unittest.TestCase):

    user = User()
    o_id = '{}.{}'.format('User', user.id)

    def setUp(self):
        self.objects = storage.all()

    def test_class(self):
        self.assertTrue(isinstance(self.user, User))

    def test_field_first_name(self):
        d = self.objects[self.o_id]
        self.assertTrue(any(k == 'first_name' for k in d.keys()))

    def test_field_last_name(self):
        d = self.objects[self.o_id]
        self.assertTrue(any(k == 'last_name' for k in d.keys()))

    def test_field_email(self):
        d = self.objects[self.o_id]
        self.assertTrue(any(k == 'email' for k in d.keys()))

    def test_field_password(self):
        d = self.objects[self.o_id]
        self.assertTrue(any(k == 'password' for k in d.keys()))

    def test_update(self):
        cur_time = self.objects[self.o_id]['updated_at']
        self.user.save()
        new_time = self.user.to_dict()['updated_at']
        self.assertNotEqual(cur_time, new_time)

    def test_load_from_dict(self):
        new = User(**self.objects[self.o_id])
        self.assertEqual(new.to_dict(), self.objects[self.o_id])

    def test_no_private_attrs(self):
        for k in self.objects[self.o_id].keys():
            if k is not '__class__':
                self.assertTrue(('__' not in k))

    def test_class_attr(self):
        self.assertEqual(self.objects[self.o_id]['__class__'], 'User')
