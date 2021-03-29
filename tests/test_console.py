#!/usr/bin/python3
""" Module for testing console"""
import unittest
import MySQLdb
from console import HBNBCommand
import pep8


class test_Console(unittest.TestCase):
    """ Class to test the console """
    @classmethod
    def setUpClass(cls):
        cls.conn = MySQLdb.connect(
            host="localhost", port=3306, user="hbnb_test",
            passwd="hbnb_test_pwd", db="hbnb_test_db", charset="utf8"
        )
        cls.cur = cls.conn.cursor()
    @classmethod
    def tearDownClass(cls):
        cls.cur.close()
        cls.conn.clos()

    def test_pep8(self):
        """Check console to be pep8 compliant"""
        fchecker = pep8.Checker("console.py", show_source=True)
        file_errors = fchecker.check_all()
        self.assertEqual(file_errors, 0)

    def test_create(self):
        """Check that created objects are correctly saved to the db"""
        # Check amount of elements in table
        count_before = type(self).cur.execute("SELECT count(states.id) FROM states")
        # Create an object and upload it to the db
        HBNBCommand.do_create('create State name="California"')
        # Check amount of elements after adding a state
        count_after = type(self).cur.execute("SELECT count(states.id) FROM states")

        # Assert if count_after is greater than count_before
        self.assertGreater(count_after, count_before)
