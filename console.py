#!/usr/bin/python3
"""
Modules for HBNB console for the AirBnB clone project
"""
import cmd
from models.base_model import BaseModel
from models.city import City

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
#                obj.save()
                print(obj.id)
            except:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """
        :params line: Name of Class and id

        :usage: 
            $ show <class name>.id
            $ [class] (id) {<dict of class>}

        :return: None
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split(' ')
            try:
                cls = globals()[args[0]].__name__
                if args[1]:
                    ident = args[1]
            except KeyError:
                print("** class doesn't exist **")
            except IndexError:
                print("** instance id missing **")
            
            try:
                #temp until FileStorage is implmented
                a = {"BaseModel.42": {"id": "42"}}
                a["{}.{}".format(cls,ident)]
#                storage.all()[cls+'.'+ident]
            except KeyError:
                print("** no instance found **")
    
    def do_all(self, line=None):
        """
        :params line: Name of Class

        :usage: 
        
        :example 1:
            $ all
            $ [[BaseModel] (id) {<dict of class>}, [City] (id) {<dict of
            class>},..]
        
        :example 2:
            $ all BaseModel
            $ [[BaseModel] (id) {<dict of class>}, [BaseModel] (id) {<dict of
            class>}, ...]

        :return: None
        """
        
        ls_d = list()
        storage = {"BaseModel.42": {"id": "42"}, "BaseModel.1337": {"id": "1337"},
                "City.101": {"id": "101"}}
        if line:
            for key, v in storage.items():
                if key.startswith(line):
                    obj = globals()[line](**v)
                    ls_d.append(str(obj))
                    del obj

        else:
            for key, v in storage.items():
                arg = key.split('.')
                obj = globals()[arg[0]](**v)
                ls_d.append(str(obj))
                del obj
        print(ls_d)

if __name__ == '__main__':
    HBNBCommand().cmdloop()



