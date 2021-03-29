#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    # is relationship.back_populates
    cities = relationship("City", backref="state")

    @property
    def cities(self):
        from models import storage
        """getter attribute cities that returns the
        list of City instances with state_id"""
        state_cities = list()
        all_cities = storage.all("City")
        for key, value in all_cities.items():
            if value.state_id == self.id:
                state_cities.append(value)
        return state_cities
