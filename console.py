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


class AirBnB_Console(cmd.Cmd):
    """
    An instance AirBnB_Console command
    
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
    AirBnB_Console().cmdloop()
