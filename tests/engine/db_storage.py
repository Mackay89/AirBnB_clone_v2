#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Unit tests for FileStorage class.
"""
import MySQLdb
import os import getenv
import unittest
from models.state import State
from models.engine.db_storage import DBStorage


@unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'Not db storage')


class TestDBStorage(unittest.TestCase):
    """
    Test the DBStorage.
    """

    @classmethod
    def setUpClass(clas):
        """
        Set up for test.
        """
        clas.User = getenv("HBNB_MYSQL_USER")
        clas.Passwd = getenv("HBNB_MYSQL_PWD")
        clas.Db = getenv("HBNB_MYSQL_DB")
        clas.Host = getenv("HBNB_MYSQL_HOST")
        clas.db = MySQLdb.connect(host=clas.Host, user=clas.User, passwd=clas.Passwd, db= clas.Db, charset="utf8")
        clas.query = clas.db.cursor()
        clas.storage = DBStorage()
        clas.storage.reload()


    @classmethod
    def tearDownClass(clas):
        """
        At the end of the test this will tear it down.
        """
        clas.query.close()
        clas.db.close()


    def test_read_tables(self):
        """
        Check existing tables.
        """
        self.query.execute("SHOE TABLES")
        salida = self.query.fetchall()
        self.assertEqual(len(salida), 7)

    def test_no_element_user(self):
        """
        Check no elements in users table.
        """
        self.query.execute("SELECT * FROM users")
        salida =self.query.fetchall()
        self.assertEqual(len(salida), 0)


    def test_no_element_cities(self):
        """
        Check no elements in cities table.
        """
        self.query.execute("SELECT * FROM cities")
        salida = self.query.fetchall()
        self.assertEqual(len(salida), 0)


    def test_add(self):
        """
        Test adding an element.
        """
        self.query.execute("SELECT * FROM states")
        query_rows = self.query.fetchall()
        self.assertEqual(len(query_rows), 0)
        state = State(name="Ebonyi")
        state.save()
        self.db.autocommit(True)
        self.query.execute("SELECT *FROM states")
        query_rows = self.query.fetchall()
        self.assertEqual(len(query_rows), 1)


if __name__ == "__main__":
    unittest.main()


