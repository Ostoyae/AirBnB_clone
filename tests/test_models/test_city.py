#!/usr/bin/python3
"""
Test module for City class
"""

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """
    Unittest for City class.
    """
    
    def setUp(self):
        """
        Create an instance.
        """

        self.city = City()

    def tearDown(self):
        """
        Clean up instance.
        """

        del self.city

    def test_init(self):
        """
        Test instance created.
        """

        self.assertTrue(isinstance(self.city, City))

    def test_test(self):
        pass
