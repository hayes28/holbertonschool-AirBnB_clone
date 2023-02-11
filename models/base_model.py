#!/usr/bin/python3
"""Base Model Module"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Base Model Template for ABNB Clone"""
    def __init__(self, *args, **kwargs):
        """New Instance of BaseModel Initialized

        Args:
            *args (any): positional args
            **kwargs (dict): kv paired data
        """
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()
        if kwargs:
            for ky, vl in kwargs.items():
                if ky != '__class__':
                    setattr(self, ky, vl)
                    if ky in ('created_at', 'updated_at'):
                        setattr(self, ky, datetime.
                                strptime(vl, '%Y-%m-%dT%H:%M:%S.%f'))
        else:
            models.storage.new(self)

    def __str__(self):
        """simple string representation method"""
        bname = self.__class__.__name__
        return "[{}] ({}) {}".format(bname, self.id, self.__dict__)

    def save(self):
        """method that updates timestamp and saves"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns dictionary of BaseModel"""
        new_richard = self.__dict__.copy()
        new_richard["__class__"] = self.__class__.__name__
        new_richard["created_at"] = self.created_at.isoformat()
        new_richard["updated_at"] = self.updated_at.isoformat()
        return new_richard
