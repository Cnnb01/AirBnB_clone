#!/usr/bin/python3
"""Defining the Airbnb console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defining interpreter"""
    prompt = "(hbnb) "
      

    def emptyline(self):
        """Ignore empty spaces"""
        pass
    
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, line):
        """Terminates the loop"""
        return True
if __name__ == '__main__':
    HBNBCommand().cmdloop()
