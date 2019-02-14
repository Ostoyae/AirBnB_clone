#!/usr/bin/python3
"""Test module for State class
"""

import unittest
from models.state import State

class TestState(unittest.TestCase):
    
    def setUp(self):
        self.state = State()

    def tearDown(self):
        del self.state

    def test_init(self):
        self.assertTrue(isinstance(self.state, State))
