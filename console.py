#!/usr/bin/python3
"""Defines the HBNBCommand class"""
import cmd
import os
import shlex
import models


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    def do_EOF(self, line):
        """exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def emptyline(self):
        """Do nothing if line is empty"""
        pass
    
    def do_create(self, line):
        """Create an instance of Class and prints the id.
        Usage: Create <class name>"""
        args = shlex.split(line)
        if(len(args) == 0):
            print("**class name missing**")
            return
        try:
            cls = models.classes[args[0]]
        except KeyError:
            print("** class doesn't exist **")
            return
        
        print(cls().id)
        models.storage.save()

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id.
        Usage: show <class name> <id>"""
        args = shlex.split(line)
        allObjs = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if "{}.{}".format(args[0], args[1]) not in allObjs:
            print("** no instance found **")
            return
        key = "{}.{}".format(args[0],args[1])
        print(allObjs[key])

    def do_destroy(self, line):
        """ Deletes an instance based on
         the class name and id,
        Usage: destroy <class name> <id>"""
        args = shlex.split(line)
        allObjs = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if "{}.{}".format(args[0],args[1]) not in allObjs:
            print("** no instance found **")
            return
        key = "{}.{}".format(args[0],args[1])
        del allObjs[key]
        models.storage.save()
        
    def do_all(self, line):
        args = shlex.split(line)
        allObjs = models.storage.all()
        res = []
        if len(args) != 0 and args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        for obj in allObjs.values():
            if len(args) == 0:
                res.append(str(obj))
            elif args[0] == obj.__class__.__name__:
                res.append(str(obj))
        print(res)
        
     def do_update(self, line):
        """
        Updates an instance based on the class name and id.
        Usage: update <class name> <id> <attribute name> \"<attribute value>\"
        """
        args = shlex.split(line)
        obj_dict = models.storage.all()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in models.classes_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj = obj_dict["{}.{}".format(args[0], args[1])]
            attribute_type = type(getattr(obj, args[2], ''))
            setattr(obj, args[2], attribute_type(args[3]))
            obj.save()
        




        


if __name__ == '__main__':
    HBNBCommand().cmdloop()