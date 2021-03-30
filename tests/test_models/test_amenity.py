#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import pep8


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_pep8(self):
        """Check console to be pep8 compliant"""
        fchecker = pep8.Checker("models/test_amenity.py", show_source=True)
        file_errors = fchecker.check_all()
        self.assertEqual(file_errors, 0)
