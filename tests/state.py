#!/usr/bin/python3
"""
Unit tests for State class.
"""


import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Test case for State class.
    """

    def setUp(self):
        """
        Set up test objects.
        """
        self.state = State()


    def test_name(self):
        """
        Test if name attribute is not a string.
        """
        self.assertNotIsInstance(self.state.name, str)


if __name__ == "__main__":
    unittest.main()
