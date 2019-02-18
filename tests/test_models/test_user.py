#!/usr/bin/python3
"""Test module for User class
"""

import unittest
from models.user import User
from models import storage

class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.user = User()
        self.usr_obj = self.user.to_dict()

    def tearDown(self):
        del self.user

    def test_init(self):
        self.assertTrue(isinstance(self.user, User))

    def test_field_first_name(self):
        self.assertTrue(any(k == 'first_name' for k in self.usr_obj.keys()))

    def test_field_last_name(self):
        self.assertTrue(any(k == 'last_name' for k in self.usr_obj.keys()))

    def test_field_email(self):
        self.assertTrue(any(k == 'email' for k in self.usr_obj.keys()))

    def test_field_password(seld):
        self.assertTrue(any(k == 'password' for k in self.usr_obj.keys()))

    
