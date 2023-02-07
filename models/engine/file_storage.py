#!/usr/bin/python3
"""FILE STORAGE MODULE"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.city import City


class FileStorage:
    """FILE STORAGE CLASS"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the richard __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the Jason :P file (path: __file_path)"""
        with open(self.__file_path, mode='w', encoding='utf-8') as fred:
            rchrd = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(rchrd, fred)

    def reload(self):
        """Deserializes jason into __objects (poor jason)"""
        try:
            with open(self.__file_path, encoding='utf-8') as fred:
                richard = json.load(fred)
                for key, value in richard.items():
                    obj = eval(value['__class__'])(**value)
                    self.__objects[key] = obj

        except FileNotFoundError:
            pass
