#!/usr/bin/python3
"""
Modules for HBNB console for the AirBnB clone project
"""
import cmd
import subprocess as sp
from models.base_model import BaseModel
from models.user import User
#from models.city import City
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Class that the console derives from.
    """

    prompt = '(hbnb) '
    intro = "{}".format('''
    Holberton bnb (hbnb) console.
    version 0.0.1

    Type help or ? for list of commands.
    ''')

    objects = storage.all()

#   Allow on these classes to be made.
    validate = [
        'BaseModel',
        'User',
        'City',
        'State',
        'Place',
        'Amenity',
        'Review'
    ]

    def help_help(self):
        """ prints help details """
        print('''
        provied details on a command
            
        Usage:
            $ help <cmd>
        ''')

    def help_EOF(self):
        """ prints help details
        """
        print('\n'.join([
            'Quit command to exit the program\n',
        ]))

    def help_quit(self):
        """ prints help details"""
        print('\n'.join([
            'Quit command to exit the program\n',
        ]))

    def emptyline(self):
        """ pass if emptyline """
        pass

    def do_EOF(self, line):
        """
        Quits the console

        Args:
            line: Unsued

        :return: None
        """
        return True

    def do_quit(self, line):
        """
        Quits the console

        Args:
            line: Unsued

        :return: None
        """
        return True

    def do_clear(self, line):
        """ clears prompt """
        sp.call('clear', shell=True)

    def help_clear(self):
        """ prints help details"""
        print('''
        Clears prompt
        ''')

    def help_list(self):
        """ prints help details"""
        print('''
        List of Classes
        ''')
        for c in self.validate:
            print('\t - {}'.format(c))

    """-------------------------AirBnB commands--------------------------"""

    def do_create(self, line):
        """
        creates an instance of a class and then
        print the ID of said new class

        Args:
            line: string from stdin, should be name of Class to create

        :return: None
        """

        if line:
            try:
                assert line in self.validate
                cls = globals()[line]
                obj = cls()
                print(obj.id)
                storage.save()
            except Exception:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_create(self):
        print("""
        creates an instance of a class and then
        print the ID of said new class

        :param line: Name of class to create.

        :usage:
            $ create <class name>
        
        :example"
            $ create BaseModel
            <class id>

        :return: None
        """)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on class name and id

        Args:
            line: string from stdin

        Returns:
            None
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split(' ')
            try:
                (cls, cls_dict) = HBNBCommand.__find_class(args, self.objects)
            except Exception:
                return
            print(str(cls(**cls_dict)))

    def help_show(self):
        print("""
        Prints the string representation of an instance
        based on class name and id

        :params line: Name of Class and id

        :usage:
            $ show <class name>.id
            $ [class] (id) {<dict of class>}

        Return: 
            None
        """)

    def do_all(self, line=None):
        """
        Prints all string representation of all instances based or not on the
        class name

        Args:
            line: string from stdin

        Returns:
            None
        """
        ls_d = list()
        if line:
            for key, v in self.objects.items():
                if key.startswith(line):
                    obj = globals()[line](**v)
                    ls_d.append(str(obj))
                    del obj

        else:
            if self.objects:
                for key, v in self.objects.items():
                    obj = globals()[v['__class__']](**v)
                    ls_d.append(str(obj))
                    del obj
        if ls_d:
            print(ls_d)
        else:
            print("** class doen't exist **")

    def help_all(self):
        print('''
        Prints all string representation of all instances based or not on the
        class name

        :params line: Name of Class

        :usage: 
            $ all
        or
            $ all <Class Name>

        :example 1:
            $ all
            $ [[BaseModel] (id) {<dict of class>}, [City] (id) {<dict of \
class>},..]

        :example 2:
            $ all BaseModel
            $ [[BaseModel] (id) {<dict of class>}, [BaseModel] (id) {<dict of \
class>}, ...]

        :return: None
        ''')

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        """

        attr = dict()
        if not line:
            print("** class name missing **")
        else:
            args = line.split(' ')
            try:
                (cls, cls_dict) = HBNBCommand.__find_class(args, self.objects)
                ident = "{}.{}".format(args[0], args[1])
            except Exception:
                return

            args = args[2::]
            if len(args) > 2:  # strip away any possible extra attributes
                args = args[:2]
            for idx in range(2):
                try:
                    if idx == 0:
                        k = args[idx]
                    elif idx == 1:
                        v = args[idx]
                except IndexError:
                    if idx == 0:
                        print("** attribute name missing **")
                    elif idx == 1:
                        print("** value missing **")
                    return

            cls = cls(**cls_dict)       # create a class with dict
            cls.save()                  # Update 'updated_at' attribute
            cls_dict = cls.to_dict()    # convert class into Dict rep
            print(cls_dict)
            cls_dict.update({k: v})     # update/insert requested attribute
            self.objects[ident].update(cls_dict)  # update Objects
            print(self.objects)

    def help_update(self):
        print('''
        Update a class base on id with the given field and value.

        :params line: Class id and field to update

        :Usage:
            $ update <class name> <id> <attribute name> <attribute value>

        :return: None
        ''')

    def do_destroy(self, line):
        """
        Destroy a Class base off name and id

        :ussage:
            $ destroy <class name> <id>

        :return: None
        """
        if not line:
            print("** class name missing **")
            return
        else:
            args = line.split(' ')
            try:
                HBNBCommand.__find_class(args, self.objects)
            except Exception:
                return
        ident = "{}.{}".format(args[0], args[1])
        self.objects.pop(ident)
        storage.save()

    def help_destroy(self):
        print('''
            destroy a class base off name and id

            :usage:
                $ destroy <class name> <id>
                ''')

    @staticmethod
    def __find_class(args=[], objects={}):
        """
        This method check if an object exists in storage __objects if invalid
        agrument are pass proper exceptions will be raise else if sucessful
        will return a tuple of (class, dictionary representation)

        Tuple:
        0: Class
        1: Dictionary rep of object found in Objects.

        :return: turple(Class, Dict)
        """
        try:
            cls = globals()[args[0]]  # get class name
            ident = args[1]
        except KeyError:
            print("** class doesn't exist **")
            raise KeyError
            return
        except IndexError:
            print("** instance id missing **")
            raise IndexError
            return

        try:
            obj = objects["{}.{}".format(cls.__name__, ident)]
#                   storage.all()[cls+'.'+ident]
        except KeyError:
            print("** no instance found **")
            raise KeyError
            return
        return (cls, obj)


if __name__ == '__main__':
    """ 
    Entry point for console
    """
    HBNBCommand().cmdloop()
