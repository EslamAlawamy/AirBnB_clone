#!/usr/bin/python3
"""command interpreter."""

import cmd
import json
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):

	prompt = "(hbnb) "
	def do_quit(self, line):
		"""Quit command to exit the program
		"""
		return True

	def do_EOF(self, line):
		"""EOF command to exit the program
		"""
		print()
		return True

	def emptyline(self):
		"""don't execute anything
		"""
		pass
	def do_create(self, arg):
		"""Creates a new instance of BaseModel"""
		if arg == "BaseModel":
			obj = BaseModel()
			storage.save()
			print(obj.id)
		elif arg != "BaseModel":
			print("** class name missing **")
		else:
			print("** class doesn't exist **")

	def do_show(self, args):
		"""Prints the string representation of an instance based on the class name and"""
		splits = args.split()
		if len(splits) == 0:
			print("** class name missing **")
			return None
		elif len(splits) == 1:
			if splits[0] == "BaseModel":
				print("** instance id missing **")
				return None
			else:
				print("** class doesn't exist **")
				return None
		all_objs = storage.all()
		if f"{splits[0]}.{splits[1]}" in all_objs:
			print("{}".format(all_objs[f"{splits[0]}.{splits[1]}"]))
			return None
		print("** no instance found **")

	def do_destroy(self, args):
		"""Deletes an instance based on the class name and id"""
		splits = args.split()
		if len(splits) == 0:
			print("** class name missing **")
			return None
		elif len(splits) == 1:
			if splits[0] == "BaseModel":
				print("** instance id missing **")
				return None
			else:
				print("** class doesn't exist **")
				return None
		all_objs = storage.all()
		if f"{splits[0]}.{splits[1]}" in all_objs:
			del all_objs[f"{splits[0]}.{splits[1]}"]
			storage.save()
		else:
			print("** no instance found **")
			return None

	def do_all(self, args):
		"""Prints all string representation of all instances based or not on the class name"""
		all_objs = storage.all()
		splits = args.split()
		if splits[0] != "BaseModel":
			print("** class doesn't exist **")
		else:
			li = []
			for obj in all_objs.values():
				li.append(str(obj))
			print(li)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
