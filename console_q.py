#!/usr/bin/python3
"""
Modules for HBNB console for the AirBnB clone project
"""
import cmd
import subprocess as sp
from models.base_model import BaseModel
#from models.city import City
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    intro = "{}".format('''
    Holberton bnb (hbnb) console.
    version 0.0.1

    Type help or ? for list of commands.
    ''')

    '''
    objects = {
        "BaseModel.42": {"id": "42"},
        "BaseModel.1337": {"id": "1337"},
        "City.101": {"id": "101"}
    }
    '''
    objects = storage.all()

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

    def do_clear(self, line):
        sp.call('clear', shell=True) #calls the linux `clear` command from shell

    """-------------------------AirBnB commands--------------------------"""

    def do_create(self, line):
        """
        creates an instance of a class and then
        print the ID of said new class

        :param line: Name of class to create.

        :return: None
        """

        if line:
            try:
                cls = globals()[line]
                obj = cls()
                print(obj.id)
                storage.save()
            except Exception as err:
                print(err)
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
            <class id>
        :example"
            $ create BaseModel
            <class id>

        :return: None
        """)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on class name and id
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split(' ')
            try:
                (cls, cls_dict) = HBNBCommand.__find_class(args, self.objects)
            except Exception as err:
                print(err)
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

        :return: None
        """)

    def do_all(self, line=None):
        """
        Prints all string representation of all instances based or not on the
        class name
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
                    arg = key.split('.') # why are you splitting by . here?
                    obj = globals()[arg[0]](**v)
                    ls_d.append(str(obj))
                    del obj
        print(ls_d)

    def help_all(self):
        print('''
        Prints all string representation of all instances based or not on the
        class name

        :params line: Name of Class

        :usage:

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

#       objects = {"BaseModel.42": {"id": "42"}}
        attr = dict()
        if not line:
            print("** class name missing **")
        else:
            args = line.split(' ')
            try:
                (cls, cls_dict) = HBNBCommand.__find_class(args, self.objects)
                ident = "{}.{}".format(args[0], args[1])
            except Exception as err:
                print(err)
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
        :params line: Class id and field to update

        :Usage:
            $ update <class name> <id> <attribute name> "<attribute value>"

        TODO

        :return: None
        ''')

    def do_destroy(self, line):
        if not line:
            print("** class name missing **")
        else:
            args = line.split(' ')
            try:
                HBNBCommand.__find_class(args, self.objects)
            except Exception as err:
                print(err)
                return
        ident = "{}.{}".format(args[0], args[1])
        self.objects.pop(ident)
        storage.save()

    def help_destroy(self):
        print('''
            destroy stuff

            :usage:
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
            raise KeyError("** class doesn't exist **")
            return
        except IndexError:
            raise IndexError("** instance id missing **")
            return

        try:
            obj = objects["{}.{}".format(cls.__name__, ident)]
#                   storage.all()[cls+'.'+ident]
        except KeyError:
            raise KeyError("** no instance found **")
            return
        return (cls, obj)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
