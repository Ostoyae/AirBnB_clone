#!/usr/bin/python3
"""
Modules for HBNB console for the AirBnB clone project
"""
import cmd
import subprocess as sp
import re
import contextlib
import io
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Console loop that acts as
    a CLI interpreter.
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
        """
        Prints help details
        after interpreter gets
        the `help` command.
        """

        print('''
        provied details on a command

        Usage:
            $ help <cmd>
        ''')

    def help_EOF(self):
        """
        Prints help details
        after interpreter gets
        the `EOF` command.
        """

        print('\n'.join([
            'Quit command to exit the program\n',
        ]))

    def help_quit(self):
        """
        Prints help details
        after the interpreter
        gets the `help` command.
        """

        print('\n'.join([
            'Quit command to exit the program\n',
        ]))

    def emptyline(self):
        """
        Pass on empty line.
        """

        pass

    def do_EOF(self, line):
        """
        Quits the console.

        Args:
            line: Interpreter input

        Return:
            None
        """

        return True

    def do_quit(self, line):
        """
        Quits the console.

        Args:
            line: Interpreter input

        Return:
            None
        """

        return True

    def do_clear(self, line):
        """
        Creates a subprocess to
        execute the `clear` command
        from the Linux shell.

        Args:
            line: Interpreter input

        Return:
            None
        """

        sp.call('clear', shell=True)

    def help_clear(self):
        """
        Prints out help details
        for the `clear` command.
        """

        print('''
        Clears prompt
        ''')

    def help_list(self):
        """
        Prints out a list of
        the possible subclasses.
        """

        print('''
        List of Classes
        ''')

        for c in self.validate:
            print('\t - {}'.format(c))

    def precmd(self, line):
        """
        Method executed just before the command line `line` is interpreted,
        This method will Check if the user Want to use a Subclass action on a
        Class instance

        Args:
            line: Classname of string type from STDIN.

        Returns:
            processed string of type String
        """

        parse = re.split(r"[.()]", line.strip())
        if parse[0] in self.validate and len(parse) > 1:
            try:
                self.__class__.__dict__[parse[1]](self, parse)
            except KeyError:
                return ''  # invokes emptyline
            return ''  # invokes emptyline

        return line.strip()  # sends line onto cmd.onecmd() as inteneded

    def all(self, obj):
        """
        Subclass action method for displaying all of the instances
        of a class.

        Args:
            obj: List of a parsed line [0: Classname, 1: action]

        Return:
            None
        """

        self.get_all(obj[0], False)

    def count(self, obj):
        """
        Subclass action method for count the number of the Class currently
        existing.

        Args:
            obj: List of a parsed line [0: ClassName]

        Return:
            None
        """

        count = 0
        with contextlib.redirect_stdout(io.StringIO()):  # supresses print()
            count = self.get_all(obj[0])
        print(count)

    def show(self, obj):
        """
        Subclass action method to show an instance by ID.

        Args:
            obj: List of parse line [0: Classname, 1: action, 2: ID]

        Return:
            None
        """

        self.do_show("{} {}".format(obj[0], obj[2][1:-1]))

    def destroy(self, obj):
        """
        Subclass action method for destroy a Class that currently exists via id

        Args:
            obj: List of a parse line [0: Classname, 1: action, 2: ID]

        Return:
            None
        """

        self.do_destroy("{} {}".format(obj[0], obj[2][1:-1]))

    def update(self, obj):
        """
        Subclass action method for updating a Class via ID.

        Args:
            obj: List of parse line [0: class, 1: action, 2: unparsed values]

        Return:
            None
        """
        a_id, field, val = (s.strip() for s in obj[2].split(','))
#        print(obj[0])
#        print("{} {} {}".format(a_id, field, val))
        self.do_update("{} {} {} {}".format(
            obj[0],
            a_id[1:-1],
            field[1:-1],
            val
            ))

    """-------------------------AirBnB commands--------------------------"""

    def do_create(self, line):
        """
        Creates an instance of a class and then
        prints the ID of said new class.

        Args:
            line: Classname of string type from STDIN.

        Raises:
            exception: Prints error code if class DNE.

        Return:
            None
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
        """
        Prints out help details
        for the `create` command.
        """

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
        based on class name and id.

        Args:
            line: Classname of string type from STDIN.

        Raises:
            Exception: Return on invalid classname

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
        """
        Prints out help details
        for the `show` command.
        """

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
        Wrapper function for `all` for that the console.

        Args:
            line: Classname of string type from STDIN

        Returns:
            None
        """
        self.get_all(line)

    def get_all(self, line=None, as_str=True):
        """
        Stores class attributes in a list
        organized according to their corresponding
        class.

        Args:
            line: Classname of string type from STDIN.
            as_str: picks which STDOUT format to use.

        Returns:
            Int: count
        """

        ls_d = list()
        count = 0

        if line:
            for k, v in self.objects.items():
                if k.startswith(line):
                    obj = globals()[line](**v)
                    ls_d.append(str(obj))
                    count += 1
                    del obj

        else:
            if self.objects:
                for k, v in self.objects.items():
                    obj = globals()[v['__class__']](**v)
                    ls_d.append(str(obj))
                    count += 1
                    del obj

        if ls_d:
            if as_str:
                print(ls_d)
            else:
                print('[', end='')
                for i, v in enumerate(ls_d):
                    print(v, end='{}'.format(
                        ', ' if i < (len(ls_d) - 1) else '')
                    )
                print(']')
            return count
        else:
            print("** class doen't exist **")

    def help_all(self):
        """
        Prints out help details
        for the `all` command.
        """

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
        Updates an instance based on the
        `classname` and `ID` by adding/updating
        attributes.

        Args:
            line: Classname of string type from STDIN.

        Raises:
            Exception: Class not found.

        Returns:
            None
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
                        try:
                            assert(float(args[idx]))
                            v = float(args[idx])
                            assert(int(args[idx]))
                            v = int(args[idx])
                        except:
                            if type(v) is not float and type(v) is not int:
                                if v[0] is '"' and v[-1] is '"':
                                    v = v[1:-1]

                except IndexError:

                    if idx == 0:
                        print("** attribute name missing **")

                    elif idx == 1:
                        print("** value missing **")

                    return

            cls = cls(**cls_dict)       # create a class with dict
            cls.save()                  # Update 'updated_at' attribute
            cls_dict = cls.to_dict()    # convert class into Dict rep
            cls_dict.update({k: v})     # update/insert requested attribute
            self.objects[ident].update(cls_dict)  # update Objects
            storage.save()

    def help_update(self):
        """
        Prints out help details
        for the `show` command.
        """

        print('''
        Update a class base on id with the given field and value.

        :params line: Class id and field to update

        :Usage:
            $ update <class name> <id> <attribute name> <attribute value>

        :return: None
        ''')

    def do_destroy(self, line):
        """
        Remove a class by `name` and `ID`

        Args:
            line: Classname/ID of string/int type from STDIN.

        Raises:
            Exception: Class not found.

        Return:
            None
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
        """
        Prints out help details
        for the `destroy` command.
        """

        print('''
            destroy a class base off name and id

            :usage:
                $ destroy <class name> <id>
                ''')

    @staticmethod
    def __find_class(args=[], objects={}):
        """
        Checks if an object exists in storage `__objects`.

        Args:
            args: Holds classname.
            object: Holds attributes of the class.

        Raises:
            KeyError: Invalid classname
            IndexError: Instance ID DNE

        Returns:
            A tuple of (class, {attributes})
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
