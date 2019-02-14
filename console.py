#!/usr/bin/python3
"""
Modules for HBNB console for the AirBnB clone project
"""
import cmd


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
        return True

    def do_quit(self, line):
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
