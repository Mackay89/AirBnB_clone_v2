#!/usr/bin/python3
"""
Unit tests for Amenity class.
"""


import unittest
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity


class TestAmenity(TestBaseModel):
    """
    TestAmenity class.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize TestAmenity class.
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity


    def test_name(self):
        """
        Test name atribute.
        """
        new = self.value()
        self.assertNotIsInstance(new.amenity.name, str)


if __name__ == "__main__":
    unittest.main()
