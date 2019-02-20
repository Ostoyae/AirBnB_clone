#!/usr/bin/python3
"""
Test module for State class
"""

import os
import pep8
import unittest
from models.state import State
from models import storage


class TestState(unittest.TestCase):
    """
    Unittest for State instance.
    """

    state = State()
    o_id = '{}.{}'.format('State', state.id)

    def setUp(self):
        self.objects = storage.all()

    def tearDown(self):
        pass

    def test_style_check(self):
        pep8style = pep8.StyleGuide(quiet=True)
        p = pep8style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_attr(self):
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)

    def test_documentation(self):
        self.assertIsNotNone(State.__doc__)

    def test_class(self):
        self.assertTrue(isinstance(self.state, State))

    def test_id(self):
        self.assertTrue(type(self.state.id), int)

    def test_name(self):
        self.assertTrue(type(self.state.name), str)

    def test_class(self):
        self.assertTrue(isinstance(self.state, State))

    def test_field_name(self):
        d = self.objects[self.o_id].to_dict()
        self.assertTrue(any(k == 'name' for k in d.keys()))

    def test_update(self):
        cur_time = self.state.updated_at
        self.state.save()
        new_time = self.state.updated_at
        self.assertNotEqual(cur_time, new_time)

    def test_load_from_dict(self):
        new = State(**self.objects[self.o_id].to_dict())
        self.assertEqual(new.to_dict(), self.objects[self.o_id].to_dict())

    def test_no_private_attrs(self):
        for k in self.objects[self.o_id].to_dict().keys():
            if k is not '__class__':
                self.assertTrue(('__' not in k))

    def test_class_attr(self):
        self.assertEqual(
                self.objects[self.o_id].to_dict()['__class__'],
                'State'
                )
