#!/usr/bin/python3
"""
Test module for State class
"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Unittest for State instance.
    """

    def setUp(self):
        """
        Create an instance.
        """

        self.state = State()

    def tearDown(self):
        """
        Clean up an instance.
        """

        del self.state

    def test_init(self):
        """
        Test instance created.
        """

        self.assertTrue(isinstance(self.state, State))
