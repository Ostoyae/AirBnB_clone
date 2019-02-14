#!/usr/bin/python3
"""
Modules for HBNB console for the AirBnB clone project
"""
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def help_help(self):
        print('\n'.join([
            'provied details on a command',
            'Usage:'
            '\n\thelp <cmd>'
        ]))

    def help_EOF(self):
        print('\n'.join([
            'Quit command to exit the program\n',
        ]))

    def help_quit(self):
        print('\n'.join([
            'Quit command to exit the program\n',
        ]))

    def emptyline(self):
        pass

    def do_EOF(self, line):
        """
        Quits the console

        :param line: Unsued

        :return: None
        """
        return True

    def do_quit(self, line):
        """
        Quits the console

        :param line: Unsued

        :return: None
        """
        return True

    def do_create(self, line):
        """
        creates an instance of a class
        
        :param line: Name of class to create.

        :return: None
        """

        if line:
            try:
                cls = globals()[line]
                obj = cls()
                # TODO: conver to json add to file and read ID
                storage.new(obj)
                storage.save()
            except:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
