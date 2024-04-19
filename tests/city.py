#!/usr/bin/python3
"""
Unit tests for City class.
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test cases for  City class.
    """


    def setUP(self):
        """
        Set up test objects.
        """
        self.city = City()


    def test_state_id(self):
        """
        Test if state_id attribute is not a string.
        """
        self.assertNotIsInstance(self.city.state_id, str)


    def test_name(self):
        """
        Test if name attribute is not a string.
        """
        self.assertNotIsInstance(self.city.name, str)


if __name__ == "__main__":
    unittest.main()
