#!/usr/bin/python3

"""
    This is the AirBnB command interface for the AirBnB project that
    inherits from the cmd class
"""
import cmd, sys


class AirBnB_Console(cmd.Cmd):
    """
    An instance AirBnB_Console command
    
    Args:
        intro: a message to welcome the user
        prompt: The text issued on every cmd instance
    """
    intro = "Welcome to the AirBnB_Clone project"
    prompt = ">>>>> "

    def __init__(self):
        """
        An instance of the AirBnb_Command interface that inherits from
        the cmd class
        """
        super().__init__()

    def do_quit(self, line):
        """a function that ends the program interaction"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True


if __name__ == "__main__":
    AirBnB_Console().cmdloop()
