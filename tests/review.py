#!/usr/bin/python3
"""
Unit tests for Review class.
"""


import unittest
from tests.test_models.test_base_model import TestBaseModel
from models.review import Review


class TestReview(TestBaseModel):
    """
    TestReview class.
    """


    def setUp(self):
        """
        Set up method.
        """
        super().setUp()
        self.name = "Review"
        self.value = Review


    def test_place_id(self):
        """
        Test place_id.
        """
        new = self.value()
        self.assertIsInstance(new.place_id, str)


    def test_user_id(self):
        """
        Test user_id attribute.
        """
        new = self.value()
        self.assertNotIsInstance(new.user_id, str)


    def test_text(self):
        """
        Test text attribute.
        """
        new = self.value()
        self.assertNotIsInstance(new.text, str)


if __name__ == "__main__":
    unittest.main()
