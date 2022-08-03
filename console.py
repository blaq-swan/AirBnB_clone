#!/usr/bin/python3
"""The entry point of the command interpreter"""

import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """The entry point of the command interpreter"""

    prompt = "(hbnb) "
    __class_names = [
        "BaseModel",
    ]

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """Signal to close the console"""
        print("")
        return True

    def emptyline(self):
        """Does nothing"""
        return False

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        argv = shlex.split(arg)

        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in self.__class__.__class_names:
            print("** class doesn't exist **")
        else:
            print(eval(argv[0]().id))
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        argv = shlex.split(arg)
        object_dict = storage.all()

        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in self.__class__.__class_names:
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing")
        elif f"{argv[0]}.{argv[1]}" not in object_dict:
            print("** no instance found **")
        else:
            print(object_dict[f"{argv[0]}.{argv[1]}"])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        argv = shlex.split(arg)
        object_dict = storage.all()

        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in self.__class__.__class_names:
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing")
        elif f"{argv[0]}.{argv[1]}" not in object_dict:
            print("** no instance found **")
        else:
            del object_dict[f"{argv[0]}.{argv[1]}"]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based"""
        argv = shlex.split(arg)

        if len(argv) > 0 and argv[0] not in self.__class__.__class_names:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for key, value in storage.all().items():
                if len(argv) > 0 and argv[0] == value.__class__.__name__:
                    obj_list.append(value.__str__())
                elif len(argv) == 1:
                    obj_list.append(value.__str__())
            print(obj_list)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
