#!/usr/bin/python3
"""console module"""
import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
