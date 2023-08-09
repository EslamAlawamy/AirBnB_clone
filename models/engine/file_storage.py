#!/usr/bin/python3
""" Store first object """
import json


class FileStorage:
	""" class FileStorage """

	__file_path = "file.json"
	__objects = {}

	def all(self):
		""" returns the dictionary __objects """
		return FileStorage.__objects

	def new(self, obj):
		""" sets in __objects the obj with key <obj class name>.id """
		key = obj.__class__.__name__ + "." + obj.id
		FileStorage.__objects[key] = obj

	def save(self):
		""" serializes __objects to the JSON file (path: __file_path) """
		dictionary = {}
		for key, value in FileStorage.__objects.items():
        	    dictionary[key] = value.to_dict()

		with open(FileStorage.__file_path, 'w') as f:
           		json.dump(dictionary, f)

	def reload(self):
		"""
		deserializes the JSON file
		to __objects (only if the
		JSON file (__file_path)
		"""
		with open(FileStorage.__file_path, 'r') as f:
			for key, value in json.load(f).items():
				self.new(dct[value['__class__']](**value))
