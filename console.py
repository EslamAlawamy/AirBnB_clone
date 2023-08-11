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
	def do_create(self, cls):
		"""Creates a new instance of BaseModel"""
		if cls == "BaseModel":
			obj = BaseModel()
			storage.save()
			print(obj.id)
		elif cls != "BaseModel":
			print("** class name missing **")
		else:
			print("** class doesn't exist **")
 
if __name__ == '__main__':
    HBNBCommand().cmdloop()
