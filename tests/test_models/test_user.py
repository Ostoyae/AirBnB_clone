#!/usr/bin/python3
"""Test module for User class
"""

import unittest
import os
from models.user import User
from models import storage

class TestUser(unittest.TestCase):
   
    user = User()
    uid = '{}.{}'.format('User', user.id)

    def setUp(self):
        self.objects = storage.all()

    def test_class(self):
        self.assertTrue(isinstance(self.user, User))
    
    def test_field_first_name(self):
        d = self.objects[self.uid]
        self.assertTrue(any(k == 'first_name' for k in d.keys()))

    def test_field_last_name(self):
        d = self.objects[self.uid]
        self.assertTrue(any(k == 'last_name' for k in d.keys()))

    def test_field_email(self):
        d = self.objects[self.uid]
        self.assertTrue(any(k == 'email' for k in d.keys()))

    def test_field_password(self):
        d = self.objects[self.uid]
        self.assertTrue(any(k == 'password' for k in d.keys()))

    def test_update(self):
        cur_time = self.objects[self.uid]['updated_at']
	self.user.save()
        new_time = self.user.to_dict()['updated_at']
        self.assertNotEqual(cur_time, new_time)
