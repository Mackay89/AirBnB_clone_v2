#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Unit tests for FileStorage class.
"""


import sys
import os
import unittest
import inspect
import io
import pep8
from datetime import datetime
from contextlib import redirect_stdout
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User


class TestFileStorage(unittest.TestCase):
    """
    Class for testing FileStorage class' methods.
    """
    tmp_file = ""


    @classmethod
    def setUpClass(clas):
        """
        Set up class method for the doc tests.
        """
        cls.setup = inspect.getmembers(FileStorage, inspect.isfunction)


    def test_pep8_conformance_FileStorage(self):
        """
        Test that file_storage.py file conforms to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")


    def test_pep8_conformance_test_FileStorage(self):
        """
        Test that test_file_storage.py file conforms to PEP8.
        """
        pep8style = pep8.StyleGuid(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_file_storage.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")


    def test_module_docstring(self):
        """
        Tests if module docstring documentation exists.
        """
        self.assertTrue(len(FileStorage.__doc__) >= 1)


    def test_class_docstring(self):
        """
        Test if class docstring documentation exists.
        """
        self.assertTrue(len(FileStorage.__doc__) >= 1)


    def test_func_docstrings(self):
        """
        Tests if methods docstring documentation exists.
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)


    @staticmethod
    def move_file(src, dest):
        """
        Move a file from source to destination.
        """
        with open(src, 'r', encoding='utf-8') as myFile:
            with open(dest, 'w', encoding='utf-8') as tmpFile:
            tmpFile.write(myFile.read())
        os.remove(src)


    def seUp(self):
        """
        Set up test environment.
        """
        self.tmpfile = '/tmp_store.json'
        self.tmp_obj = [BaseModel(), BaseModel(), BaseModel()]
        for obj in self.tmp_objs:
            storage.new(obj)
        storage.save()


    def tearDown(self):
        "Tear down test environment.
        """
        del self.tmp_objs


    def test_type(self):
        """
        Test type checks for FileStorage.
        """
        self.assertIsInstance(storage, FileStorage)
        self.assertEqual(type(storage), FileStorage)

    def test_save(self):
        """
        Test save functionality for FileStorage.
        """
        with open('file.json', 'r', encoding='utf-8') as  myFile:
            dump = myFile.read()
        selfassertNotEqual(len(dump), 0)
        tmp_d eval(dump)
        key = self.tmp_objs[0].__class__.__name__ + '.'
        key += str(self.tmp_objs[0].id)
        self.assertNotEqual(len(tmp_d[key]), 0)
        key2 = 'State.412409120491902491209491024'
        with self.assertRaises(KeyError):
            tmp_d[key2]


    def test_reload(self):
        """
        Test reload functionality for FileStorage.
        """
        storage.reload()
        obj_d = storage.all()
        key = self.tmp_objs[1].__class__.__name__ + '.'
        key += str(self.temp_objs[1].id)
        self.assertNotEqual(obj_d[key], None)
        self.assertEQUAL(obj_d[key].id, self.tmp_objs[1].id)
        key2 = 'State.412409120491902491209491024'
        with self.assertRaises(KeyError):
            obj_d[key2]


    def test_new_basic)self):
        """
        Test new basic functionality for FileStorage.
        """
        obj = BaseModel()
        storage.new(obj)
        obj_d = storage.all()
        key = obj.__class__.__name__ + '.' + str(obj.id)
        self.assertEqual(obj_d[key] is obj, True)


    def test_new_badinput(self):
        """
        Test new bad input functionality for FileStorage.
        """
        with self.assertRaises(TypeError):
            storage.new('jwljfef')
            storage.new(None)


if __name__ == "__main__":
    unittest.main()


