#!/usr/bin/python3
"""Base Model Module"""
import uuid
import datetime


class BaseModel:
    """Base Model Class"""
    def __init__(self):
        "SPIN UP"
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.datetime.now()

    def __str__(self):
        """STR METH"""
        return "[{}] ({}) "
        "{}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """UPDATE TIMESTAMP"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """NEW RICHARD"""
        new_richard = self.__dict__.copy()
        new_richard["__class__"] = self.__class__.__name__
        new_richard["created_at"] = self.created_at.isoformat()
        new_richard["updated_at"] = self.updated_at.isoformat()
        return new_richard
