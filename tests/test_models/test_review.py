#!/usr/bin/python3
"""
Test module for Review class.
"""

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
