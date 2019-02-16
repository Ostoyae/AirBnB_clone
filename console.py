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
                # TODO: conver to json add to file and read ID
#                obj.save()
                print(obj.id)
            except:
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
                cls = globals()[args[0]].__name__
                ident = args[1]
            except KeyError:
                print("** class doesn't exist **")
                return
            except IndexError:
                print("** instance id missing **")
                return

            try:
                # temp until FileStorage is implmented
                a = {"BaseModel.42": {"id": "42"}}
                a["{}.{}".format(cls, ident)]
#                storage.all()[cls+'.'+ident]
            except KeyError:
                print("** no instance found **")

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
        # TODO: use storage.all() once available
        storage = {
                "BaseModel.42": {"id": "42"},
                "BaseModel.1337": {"id": "1337"},
                "City.101": {"id": "101"}
                }
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
        
        objects = {"BaseModel.42": {"id": "42"}}
        
        if not line:
            print("** class name missing **")
        else:
            args = line.split(' ')
            try:
                find_class(args, objects)
            except Exception as err:
                print("err")
                return
            try:
                args = args[2::]
            
                for val, idx in enumerate(args): 
                    try:
                        if idx == 1:
                            params['attr_n'] = val
                        elif idx == 2:
                            params['value'] = val
                        else:
                            raise IndexError
                    except indexerror:
                            print(error_msg[idx + 2])
                            return
            except Exception:
                pass


    def help_update(self):
        print('''
        :params line: Class id and field to update

        :Usage:
            $ update <class name> <id> <attribute name> "<attribute value>"

        TODO

        :return: None
        ''')

    @staticmethod
    def find_class(args=[], objects={}):
        try:
            globals()[args[0]].__name__  # get class name
            ident= args[1]
        except KeyError:
            raise IndexError("** class doesn't exist **")
        except IndexError:
            raise IndexError("** instance id missing **")
        finally:
            try:
                objects["{}.{}".format(params['class'], params['id'])]
#                   storage.all()[cls+'.'+ident]
            except KeyError:
                raise KeyError("** no instance found **")
       


if __name__ == '__main__':
    HBNBCommand().cmdloop()
