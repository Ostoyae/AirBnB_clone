#!/usr/bin/python3
"""Test module for Amenity class
"""

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    
    def setUp(self):
        self.amenity = Amenity()

    def tearDown(self):
        del self.amenity

    def test_init(self):
        self.assertTrue(isinstance(self.amenity, Amenity))
