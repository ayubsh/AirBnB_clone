#!/usr/bin/python3
""" Console cmd Module """
import cmd


class HBNBCommand(cmd.Cmd):
    """ console program """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Exit method - type quit to exit """
        return True

    def do_EOF(self, args):
        """Exit method for EOF """
        return True

    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
