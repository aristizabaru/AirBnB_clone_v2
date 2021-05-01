#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """getter attribute cities that returns the
            list of City instances with state_id"""
            from models import storage
            state_cities = list()
            all_cities = storage.all("City")
            for key, value in all_cities.items():
                if value.state_id == self.id:
                    state_cities.append(value)
            return state_cities
