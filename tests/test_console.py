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

    def test_pep8(self):
        """Check console to be pep8 compliant"""
        fchecker = pep8.Checker("console.py", show_source=True)
        file_errors = fchecker.check_all()
        self.assertEqual(file_errors, 0)

    def test_create(self):
        """Test create"""
        stdout = None
        with patch('sys.stdout', new=io.StringIO()) as fd:
            HBNBCommand().onecmd('create State name="California"')
            stdout = fd.getvalue()
            self.assertEqual(type(stdout), str)
