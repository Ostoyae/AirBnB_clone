#!/usr/bin/python3
"""Test module for Place class
"""

import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    
    def setUp(self):
        self.place = Place()

    def tearDown(self):
        del self.place

    def test_init(self):
        self.assertTrue(isinstance(self.place, Place))
