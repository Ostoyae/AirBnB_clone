#!/usr/bin/python3
"""Test module for City class
"""

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    
    def setUp(self):
        self.city = City()

    def tearDown(self):
        del self.city

    def test_init(self):
        self.assertTrue(isinstance(self.city, City))

    def test_test(self):
        pass
