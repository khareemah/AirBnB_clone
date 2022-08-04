#!/usr/bin/python3
""" A Command Interpreter Class.

"""

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Defines instance attribute for Command Interpreter Class.

    """

    def __init__(self):
        """ Initializes the object. """
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """ """
        return True

    def emptyline(self):
        """ Empty line plus enter shouldnt execute anything. """
        pass

    def do_create(self, line):
        """ Creates a new instance of BaseModel. """
        if not line:
            print("**class name missing **")
        else:
            line = line.split()
            if line[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                new_instance = BaseModel()
                print(new_instance.id)
                new_instance.save()

    def do_show(self, line):
        """ Print string representation of an instance. """
        if not line:
            print("** class name missing **")
        else:
            line = line.split()
            line_len = len(line)
            if line[0] != "BaseModel":
                print("** class doesn't exist**")
            elif line_len < 2:
                print("** instance id missing **")
            elif (new_instance.id != id):
                print("** no instance found **")
            else:
                pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
