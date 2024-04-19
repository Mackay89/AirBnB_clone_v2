#!/usr/bin/python3
"""
Unit tests for User class.
"""
from unittest 
from models.user import user


class TestUser(unittest.TestCase):
    """
    Represent test cases for User class.
    """


    def setUp(self):
        """
        Set up test objects.
        """
        self.user = User()


    def test_first_name(self):
        """
        Test if first_name attribute is a string.
        """
        self.assertIsInstance(self.user.first_name, str)


    def test_last_name(self):
        """
        Test if last_name attribute is a string.
        """
        self.assertIsInstance(self.user.email, str)


    def test_password(self):
        """
        Test if password attribute is a string.
        """
        self.assertIsInstance(self.user.password, str)


if __name__ == "__main__":
    unittest.main()

