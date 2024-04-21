#!/usr/bin/python3
"""
Module that tests console.
"""
import os 
import unittest
from unittest.mock import patch
from io import StringIO
import console
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """
    Represent the test Suite for the console.
    """


    @classmethod 
    def setUpClass(clas):
        """
        Setup for test.
        """
        clas.console = HBNBCommand()


    def tearDownClass(clas):
        """
        At the end of the test this will tear it down.
        """
        del clas.console


    def tearDown(self):
        """
        Remove temporary file (file.json) created as a result.
        """
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            try:
                os.remove("file.json")
            except exception:
                pass


    def test_docstrings_in_console(self):
        """
        Checking for docstrings.
        """
        self.assertNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do._destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)


    def test_empyline(self):
        """
        Test empty line.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("\n")
            self.assertEqual('', f.getvalue())


if __name__ == "__main__":
    unittest.main()
