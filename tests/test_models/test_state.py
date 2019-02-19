#!/usr/bin/python3
"""
Test module for State class
"""

import unittest
from models.state import State
from models import storage


class TestState(unittest.TestCase):
    """
    Unittest for State instance.
    """

    user = State()
    o_id = '{}.{}'.format('State', user.id)

    def setUp(self):
        self.objects = storage.all()

    def test_class(self):
        self.assertTrue(isinstance(self.user, State))

    def test_field_name(self):
        d = self.objects[self.o_id]
        self.assertTrue(any(k == 'name' for k in d.keys()))

    def test_update(self):
        cur_time = self.objects[self.o_id]['updated_at']
        self.user.save()
        new_time = self.user.to_dict()['updated_at']
        self.assertNotEqual(cur_time, new_time)

    def test_load_from_dict(self):
        new = State(**self.objects[self.o_id])
        self.assertEqual(new.to_dict(), self.objects[self.o_id])

    def test_no_private_attrs(self):
        for k in self.objects[self.o_id].keys():
            if k is not '__class__':
                self.assertTrue(('__' not in k))

    def test_class_attr(self):
        self.assertEqual(self.objects[self.o_id]['__class__'], 'State')
