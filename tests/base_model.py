#!/usr/bin/python3
"""
Unit tests for BaseModel class.
"""


import unittest
from models.base_model import BaseModel
import datetime
import json
import os


class TestBaseModel(unittest.TestCase):
    """
    TestBaseModel class.
    """


    def setUp(self):
        """
        Set up method.
        """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass


    def tearDown(self):
        """
        Tear down method.
        """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass


    def test_default(self):
        """
        Test default initialization.
        """
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)


    def test_kwargs(self):
        """
        Test initialization with kwargs.
        """
        obj = BaseModel()
        obj_dict = obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        self.assertNotEqual(obj, new_obj)


    def test_kwargs_int(self):
        """
        Test initialization with integer kwargs.
        """
        obj = BaseModel()
        obj_dict = obj.to_dict()
        obj_dict[1] = 2
        with self.assertRaises(TypeError):
            new_obj = BaseModel(**obj_dict)


    def test_save(self):
        """
        Test save method.
        """
        obj = BaseModel()
        obj.save()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        with open('file.json', 'r') as f:
            data = json.load(f)
            self.assertEqual(data[key], obj.to_dict())


    def test_str(self):
        """
        Test __str__ method.
        """
        obj = BaseModel()
        self.assertEqual(str(obj), "[{}] ({}) {}".format(obj.__class__.__name__, obj.__dict__))


    def test_to_dict(self):
        """
        Test to_dict method.
        """
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')


    def test_kwargs_none(self):
        """
        Test initialization with None kwargs.
        """
        obj_dict = {None: None}
        with self.assertRaises(TypeError):
            new_obj = BaseModel(**obj_dict)


    def test_id(self):
        """
        Test id attribute.
        """
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)


    def test_created_at(self):
        """
        Test created_at attribute.
        """
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime.datetime)


    def test_updated_at(self):
        """
        Test updated_at attribute.
        """
        Obj = BaseModel()
        self.assertIsInstance(obj.updated_at, datetime,datetime)
        self.assertNotEqual(obj.created_at, obj.updated_at)


if __name__ == "__main__":
    unittest.main()
