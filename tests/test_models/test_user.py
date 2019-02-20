#!/usr/bin/python3
"""Test module for User class
"""

import os
import pep8
import unittest
from models.user import User
from models import storage


class TestUser(unittest.TestCase):

    user = User()
    o_id = '{}.{}'.format('User', user.id)

    def setUp(self):
        """
        setup test
        """

        self.objects = storage.all()

    def tearDown(self):
        """
        tearDown
        """"

        pass

    def test_style_check(self):
        """
        check for pep8 compliant
        """

        pep8style = pep8.StyleGuide(quiet=True)
        p = pep8style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_attr(self):
        """
        test for BaseModel attrs
        """

        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)

    def test_documentation(self):
        """
        test for docs
        """

        self.assertIsNotNone(User.__doc__)

    def test_class(self):
        """
        test if a class was instance correctly
        """

        self.assertTrue(isinstance(self.user, User))

    def test_id(self):
        """
        test for id attribute
        """
        self.assertTrue(type(self.user.id), int)

    def test_field_first_name(self):
        """
        Test pub class attr 'first_name' was impl
        """

        d = self.objects[self.o_id]
        self.assertTrue(any(k == 'first_name' for k in d.keys()))

    def test_field_last_name(self):
        """
        Test pub class attr was last_name impl
        """

        d = self.objects[self.o_id]
        self.assertTrue(any(k == 'last_name' for k in d.keys()))

    def test_field_email(self):
        """
        Test pub class attr was email impl
        """

        d = self.objects[self.o_id]
        self.assertTrue(any(k == 'email' for k in d.keys()))

    def test_field_password(self):
        """
        Test pub class attr password was impl
        """

        d = self.objects[self.o_id]
        self.assertTrue(any(k == 'password' for k in d.keys()))

    def test_update(self):
        """
        test updating updated_at
        """

        cur_time = self.objects[self.o_id]['updated_at']
        self.user.save()
        new_time = self.user.to_dict()['updated_at']
        self.assertNotEqual(cur_time, new_time)

    def test_load_from_dict(self):
        """
        test load User from dictionary
        """

        new = User(**self.objects[self.o_id])
        self.assertEqual(new.to_dict(), self.objects[self.o_id])

    def test_no_private_attrs(self):
        """
        test that no private class var were added from User
        """

        for k in self.objects[self.o_id].keys():
            if k is not '__class__':
                self.assertTrue(('__' not in k))

    def test_class_attr(self):
        """
        Test storaged object is class User
        """

        self.assertEqual(self.objects[self.o_id]['__class__'], 'User')
