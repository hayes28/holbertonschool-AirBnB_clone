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

    def do_show(self, line):
        if line == "":
            print("** class name missing **")
            return
        args = line.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name, id = args[0], args[1]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        objects = models.storage.all()
        key = "{}.{}".format(class_name, id)
        if key not in objects:
            print("** no instance found **")
            return
        obj = objects[key]
        print(obj)

    def do_destroy(self, line):
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        cname = args[0]
        uwuid = args[1]
        cls_lst = ["Review", "Place", "State", "User", "BaseModel", "City", "Amenity"]
        if cname not in cls_lst:
            print("** class doesnt exist **")
            return
        target = "{}.{}".format(cname, uwuid)
        if target not in storage.all().keys():
            print("** no instance found **")
        storage.remove(target)
        storage.save()
        return

    def do_all(self, line):
        if line == "":
            print([str(ii) for ii in storage.all().values()])
            return
        cls_lst = ["Review", "Place", "State", "User", "BaseModel", "City", "Amenity"]
        if line in cls_lst:
            print([str(ii) for ik, ii in storage.all().items() if line in ik])
        else:
            print("** class doesnt exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
