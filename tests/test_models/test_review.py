#!/usr/bin/python3
"""
Test module for Review class.
"""

import os
import pep8
import unittest
from models.review import Review
from models import storage


class TestReview(unittest.TestCase):
    """
    Unittest for Review class.
    """

    review = Review()
    o_id = '{}.{}'.format('Review', review.id)

    def setUp(self):
        self.objects = storage.all()

    def tearDown(self):
        try:
            os.remove("file.json")

        except FileNotFoundError:
            pass

    def test_style_check(self):
        pep8style = pep8.StyleGuide(quiet=True)
        p = pep8style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_attr(self):
        self.assertTrue('id' in self.review.__dict__)
        self.assertTrue('created_at' in self.review.__dict__)
        self.assertTrue('updated_at' in self.review.__dict__)

    def test_documentation(self):
        self.assertIsNotNone(Review.__doc__)

    def test_class(self):
        self.assertTrue(isinstance(self.review, Review))

    def test_id(self):
        self.assertTrue(type(self.review.id), int)

    def test_class(self):
        self.assertTrue(isinstance(self.review, Review))

    def test_field_place_id(self):
        d = self.objects[self.o_id]
        self.assertTrue(any(k == 'place_id' for k in d.keys()))

    def test_field_text(self):
        d = self.objects[self.o_id]
        self.assertTrue(any(k == 'text' for k in d.keys()))

    def test_field_user_id(self):
        d = self.objects[self.o_id]
        self.assertTrue(any(k == 'user_id' for k in d.keys()))

    def test_update(self):
        cur_time = self.objects[self.o_id]['updated_at']
        self.review.save()
        new_time = self.review.to_dict()['updated_at']
        self.assertNotEqual(cur_time, new_time)

    def test_load_from_dict(self):
        new = Review(**self.objects[self.o_id])
        self.assertEqual(new.to_dict(), self.objects[self.o_id])

    def test_no_private_attrs(self):
        for k in self.objects[self.o_id].keys():
            if k is not '__class__':
                self.assertTrue(('__' not in k))

    def test_class_attr(self):
        self.assertEqual(self.objects[self.o_id]['__class__'], 'Review')
