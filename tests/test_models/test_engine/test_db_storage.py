#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
import pep8


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """
    def test_pep8(self):
        """Check db_storage to be pep8 compliant"""
        fchecker = pep8.Checker("models/engine/db_storage.py", show_source=True)
        file_errors = fchecker.check_all()
        self.assertEqual(file_errors, 0)
