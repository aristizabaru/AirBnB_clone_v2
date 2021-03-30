#!/usr/bin/python3
""" Module for testing console"""
import unittest
import MySQLdb
from console import HBNBCommand
from models import storage
from unittest.mock import patch
import os
import io
import pep8


class test_Console(unittest.TestCase):
    """ Class to test the console """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass

    def test_pep8(self):
        """Check console to be pep8 compliant"""
        fchecker = pep8.Checker("console.py", show_source=True)
        file_errors = fchecker.check_all()
        self.assertEqual(file_errors, 0)

    def test_create(self):
        """Test <help> <help>"""
        with patch('sys.stdout', new=io.StringIO()) as fd:
            HBNBCommand().do_create('State name="California"')
            stdout = fd.getvalue()
            loaded = None
            for obj in storage.all().values():
                loaded = obj
            self.assertEqual(str(loaded.to_dict()['id']) + '\n', stdout)
            self.assertEqual(loaded.to_dict()['name'], "California")
