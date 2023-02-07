#!/usr/bin/python3
"""console module"""
import cmd
import models.base_model
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNB Com Class"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """escape hatch"""
        return True

    def do_EOF(self, line):
        """give AOL message"""
        print("Goodbye")
        return True

    def emptyline(self):
        """no do stuff if empty line"""
        pass

    def do_create(self, line):
        if line == "":
            print("** class name missing **")
            return
        class_name = line.split()[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        new_obj = eval(class_name + "()")
        new_obj.save()
        print(new_obj.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
