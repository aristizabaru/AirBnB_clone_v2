#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
import pep8
import io
from unittest.mock import patch
from console import HBNBCommand


class test_dbStorage(unittest.TestCase):
    """ Class to test the db storage method """

    def test_pep8(self):
        """Check db_storage to be pep8 compliant"""
        fchecker = pep8.Checker(
            "models/engine/db_storage.py", show_source=True)
        file_errors = fchecker.check_all()
        self.assertEqual(file_errors, 0)

    def test_create(self):
        """Test create"""
        stdout = None
        with patch('sys.stdout', new=io.StringIO()) as fd:
            HBNBCommand().onecmd('create State name="California"')
            stdout = fd.getvalue()
            self.assertEqual(type(stdout), str)
