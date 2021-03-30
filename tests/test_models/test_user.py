#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import pep8


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value(first_name="Pablo")
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value(last_name="Montoya")
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value(email="airbnb@airbnb.com")
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value(password="123")
        self.assertEqual(type(new.password), str)

    def test_pep8(self):
        """Check console to be pep8 compliant"""
        fchecker = pep8.Checker("models/user.py", show_source=True)
        file_errors = fchecker.check_all()
        self.assertEqual(file_errors, 0)
