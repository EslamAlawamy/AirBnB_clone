#!/usr/bin/python3
""" Base Model Unittest """
import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """ TestBaseModel Unittest Class """
    def test_attributes_initialization(self):
        my_model = BaseModel()
        self.assertEqual(my_model.name, "")
        self.assertEqual(my_model.my_number, 0)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str_method(self):
        my_model = BaseModel()
        str_representation = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), str_representation)

    def test_save_method(self):
        my_model = BaseModel()
        prev_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(my_model.updated_at, prev_updated_at)

    def test_to_dict_method(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        self.assertIsInstance(my_model_json, dict)
        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertEqual(my_model_json['name'], "My First Model")
        self.assertEqual(my_model_json['my_number'], 89)
        self.assertIsInstance(datetime.strptime(my_model_json['created_at'], "%Y-%m-%dT%H:%M:%S.%f"),
                              datetime)
        self.assertIsInstance(datetime.strptime(my_model_json['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"),
                              datetime)

    def test_to_dict_with_custom_attrs(self):
        my_model = BaseModel()
        my_model.custom_attr = "Custom Value"
        my_model_json = my_model.to_dict()
        self.assertEqual(my_model_json['custom_attr'], "Custom Value")

    def test_from_dict_to_instance(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        new_model = BaseModel(**my_model_json)
        self.assertEqual(my_model.id, new_model.id)
        self.assertEqual(my_model.name, new_model.name)
        self.assertEqual(my_model.my_number, new_model.my_number)
        self.assertEqual(my_model.created_at, new_model.created_at)
        self.assertEqual(my_model.updated_at, new_model.updated_at)

if __name__ == '__main__':
    unittest.main()

