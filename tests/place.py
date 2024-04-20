#!/usr/bin/python3
"""
Unit tests for Place class.
"""


import unittest
from tests.test_models.test_base_model import TestBaseModel
from models.place import Place


class TestPlace(TestBaseModel):
    """
    TestPlace class.
    """


    def __init__(self, *args, **kwargs):
        """
        Initializes TestPlace class.
        """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place


    def test_city_id(self):
        """
        Test city_id attribute.
        """
        new = self.value()
        self.assertNotIsInstance(new.city_id, str)


    def test_user_id(self):
        """
        Test user_id attribute.
        """
        new = self.value()
        self.assertNotIsInstance(new.user_id, str)


    def test_name(self):
        """
        Test name attribute.
        """
        new = self.value()
        self.assertNotIsInstance(new.name, str)


    def test_description(self):
        """
        Test description attribute.
        """
        new = self.value()
        self.assertNotIsInstance(new.description, str)


    def test_number_rooms(self):
        """
        Test number_rooms attribute.
        """
        new = self.value()
        self.assertIsInstance(new.number_rooms, int)


    def test_number_bathrooms(self):
        """
        Test number_bathrooms attribute.
        """
        new = self.value()
        self.assertIsInstance(new.number_bathrooms, int)


    def test_max_guest(self):
        """
        Test max_guest.
        """
        new = self.value()
        self.assertIsInstance(new.max_guest, int)


    def test_price_by_night(self):
        """
        Test price_by_night attribute.
        """
        new = self.value()
        self.assertIsInstance(new.price_by_night, int)


    def test_latitude(self):
        """
        Test latitude attribute.
        """
        new = self.value()
        self.assertIsInstance(new.latitude, float)


    def test_longitude(self):
        """
        Test longitude attribute.
        """
        new = self.value()
        self.assertIsInstance(new.longitude, float)


if __name__ == "__main__":
    unittest.main()
