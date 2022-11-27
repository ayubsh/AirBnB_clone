#!/usr/bin/python3
""" Console cmd Module """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.base_model import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ console program for Airbnb"""
    classes_l = {'BaseModel': BaseModel,
                 'User': User,
                 'State': State,
                 'Review': Review,
                 'Place': Place,
                 'Amenity': Amenity,
                 'City': City
                 }
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Exit method - type quit to exit """
        return True

    def do_EOF(self, args):
        """Exit method for EOF """
        print("")
        return True

    def emptyline(self):
        """ emptyline <Enter> + emptyline """
        pass

    def do_create(self, args):
        """ Creates a new instance of BaseModel """
        if len(args) == 0:
            print("** class name missing **")
            return

        if args:
            args_l = args.split()
            if len(args_l) == 1:
                if args in self.classes_l.keys():
                    new_obj = self.classes_l[args]()
                    new_obj.save()
                    print(new_obj.id)
                else:
                    print("** class doesn't exist **")

    def do_show(self, args):
        """ Prints the string representation of an instance based on
            the class name and id
        """
        if len(args) == 0:
            print("** class name missing **")
            return
        if args:
            args_l = args.split()
            if args_l[0] not in self.classes_l.keys():
                print("** class doesn't exist **")
                return
            elif len(args_l) == 1:
                print("** instance id missing **")
                return
            else:
                key = args_l[0] + '.' + args_l[1]
                if key in storage.all():
                    st = storage.all()
                    print(st[key])
                else:
                    print("** no instance found **")
                    return

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id """
        if len(args) == 0:
            print("** class name missing **")
            return
        if args:
            args_l = args.split()
            if args_l[0] not in self.classes_l.keys():
                print("** class doesn't exist **")
                return
            elif len(args_l) == 1:
                print("** instance id missing **")
                return
            else:
                key = args_l[0] + '.' + args_l[1]
                if key in storage.all():
                    storage.all().pop(key)
                    storage.save()
                else:
                    print("** no instance found **")
                    return

    def do_all(self, args):
        """ Prints all string representation of all
        instances based or not on the class name.
        """
        if len(args) == 0:
            print([str(a) for a in storage.all().values()])
        elif args not in self.classes_l:
            print("** class doesn't exist **")
            return
        else:
            print([str(a) for (b, a) in storage.all().items() if args in b])

    def do_update(self, args):
        """ update <class name> <id> <attribute name> "<attribute value>" """
        if len(args) == 0:
            print("** class name missing **")
            return

        if args:
            args_l = args.split()
            if len(args_l) == 1:
                print("** instance id missing **")
                return
            elif len(args_l) == 2:
                print("** attribute name missing **")
                return
            elif len(args_l) == 3:
                print("** value missing **")
                return
            else:
                key = args_l[0] + '.' + args_l[1]
                if key in storage.all():
                    setattr(storage.all()[key], args[2], args[3][1:-1])
                    storage.all()[key].save()
                else:
                    print("** no instance found **")
                    return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
