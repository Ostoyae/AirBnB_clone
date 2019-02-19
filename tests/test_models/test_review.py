#!/usr/bin/python3
"""
Test module for Review class.
"""

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    
    def setUp(self):
        """
        Create an instance.
        """

        self.review = Review()

    def tearDown(self):
        """
        Clean up an instance.
        """

        del self.review

    def test_init(self):
        """
        Test instance created.
        """

        self.assertTrue(isinstance(self.review, Review))
