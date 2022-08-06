#!/usr/bin/python3
"""The entry point of the command interpreter"""

import cmd
import shlex

from models.base_model import BaseModel
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    """The entry point of the command interpreter"""

    prompt = "(hbnb) "
    __class_names = [
        "BaseModel",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review",
        "User"
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
            print(eval(argv[0])().id)
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
            print("** instance id missing **")
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
        args = shlex.split(arg)

        if len(args) > 0 and args[0] not in HBNBCommand.__class_names:
            print("** class does not exist **")
        else:
            objects = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    objects.append(str(obj))
                elif len(args) == 0:
                    objects.append(str(obj))
            print(objects)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        argv = shlex.split(arg)
        object_dict = storage.all()

        if len(argv) == 0:
            print("** class name missing **")
            return False
        if argv[0] not in self.__class__.__class_names:
            print("** class doesn't exist **")
            return False
        if len(argv) == 1:
            print("** instance id missing")
            return False
        if f"{argv[0]}.{argv[1]}" not in object_dict:
            print("** no instance found **")
            return False
        if len(argv) == 2:
            print("** attribute name missing **")
            return False
        if len(argv) == 3:
            try:
                type(eval(argv[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(argv) == 4:
            json_obj = object_dict[f"{argv[0]}.{argv[1]}"]
            if argv[2] in json_obj.__class__.__dict__.keys():
                type_val = type(json_obj.__class__.__dict__[argv[2]])
                json_obj.__dict__[argv[2]] = type_val[argv[3]]
            else:
                json_obj.__dict__[argv[2]] = argv[3]
        elif type(eval(argv[2])) == dict:
            json_obj = object_dict[f"{argv[0]}.{argv[1]}"]
            for k, v in eval(argv[2]).items():
                if (k in json_obj.__class__.__dict__.keys() and
                        isinstance(type(json_obj.__class__.__dict__[k],
                                        (str, int, float)))):
                    type_val = type(json_obj.__class__.__dict__[k])
                    json_obj.__dict__[k] = type_val[k]
                else:
                    json_obj.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
