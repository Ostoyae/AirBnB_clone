#!/usr/bin/python3
"""Test module for Review class
"""

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    
    def setUp(self):
        self.review = Review()

    def tearDown(self):
        del self.review

    def test_init(self):
        self.assertTrue(isinstance(self.review, Review))
