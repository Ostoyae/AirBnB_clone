#!/usr/bin/python3
"""
Test module for Amenity class.
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Unittest for
    Amenity class.
    """

    def setUp(self):
        """
        Creates an instance.
        """

        self.amenity = Amenity()

    def tearDown(self):
        """
        Cleans up an instance.
        """

        del self.amenity

    def test_init(self):
        """
        Test instance.
        """

        self.assertTrue(isinstance(self.amenity, Amenity))
