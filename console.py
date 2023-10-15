#!/usr/bin/python3
"""
    This is the AirBnB command interface for the AirBnB project that
    inherits from the cmd class
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.__init__ import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    An instance HBNBCommand
    
    Attributes:
        intro: a message to welcome the user
        prompt: The text issued on every cmd instance
        __classes - Contains a dictionary of all classes
    """
    intro = "Welcome to the AirBnB_Clone project"
    prompt = "(hbnb) "
    __classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                }

    def do_create(self, line):
        """
        create an instance of a class

        Args:
            line (str)- class name, parsed directly from the cmd-line
        """
        if len(line) == 0:
            print('** class name missing **')
        elif line not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_model = HBNBCommand.__classes[line]()
            new_model.save()
            print(new_model.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based
        on the class name and id
        """
        args = line.split()

        try:
            className = args[0]
            if className not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
        except:
            print("** class name missing **")
            return

        try:
            id = args[1]
        except:
            print('** instance id missing **')
            return

        key = className + "." + str(id)
        fetch_dicts = storage.all()
            
        try:
            print(fetch_dicts[key])
        except Exception as e:
            print("** no instance found **")

    def emptyline(self):
        """
        emptyline - This method called when we have an empty line.
                    If this method is not overridden,
                    it repeats the last nonempty command entered.
        """
        pass

    def do_quit(self, line):
        """a function that ends the program interaction"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
