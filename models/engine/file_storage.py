#!/usr/bin/python3
""" Store first object """
import json
from models.base_model import BaseModel

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

		with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
           		json.dump(dictionary, f, indent=2)

	def reload(self):
		"""
		deserializes the JSON file
		to __objects (only if the
		JSON file (__file_path)
		"""
		with open(self.__file_path, "r", encoding='utf-8') as f:
			json_objs = json.load(f)
                
		for key, val in json_objs.items():
			self.__objects[key] = BaseModel(**val) 
