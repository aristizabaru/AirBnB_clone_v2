#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

_format = "%Y-%m-%dT%H:%M:%S.%f"
Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    # Columns of the table
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # storage.new(self)
        else:
            # set attributes
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

            # compare created_at
            if kwargs.get("created_at", None):
                self.created_at = datetime.strptime(
                    kwargs["created_at"], _format)
            else:
                self.created_at = datetime.utcnow()

            # compare updated_at
            if kwargs.get("updated_at", None):
                self.updated_at = datetime.strptime(
                    kwargs["updated_at"], _format)
            else:
                self.updated_at = datetime.utcnow()

            # compare id and save new instance
            if kwargs.get("id", None) is None:
                from models import storage
                self.id = str(uuid.uuid4())
                # storage.new(self)
                # this method saves the new object to __objects variable
                # in storage. It does not saves them to the .json file

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        # remove this key=value only if exists
        if "_sa_instance_state" in dictionary:
            dictionary.pop("_sa_instance_state")
        return dictionary

    def delete(self):
        """Deletes de current object"""
        from models import storage
        storage.delete(self)
