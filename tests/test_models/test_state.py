#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import pep8


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_pep8(self):
        """Check console to be pep8 compliant"""
        fchecker = pep8.Checker("models/state.py", show_source=True)
        file_errors = fchecker.check_all()
        self.assertEqual(file_errors, 0)
