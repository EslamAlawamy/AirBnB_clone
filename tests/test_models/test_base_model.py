#!/usr/bin/python3
""" Unittest Base Model """
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ TestBaseModel Class """

    def test_attributes_initialization(self):
        """ test init function attributes """
        my_base = BaseModel()
        
        self.assertEqual(my_base.name, "")
        self.assertEqual(my_base.my_number, 0)
        self.assertIsInstance(my_base.id, str)
        self.assertIsInstance(my_base.created_at, datetime)
        self.assertIsInstance(my_base.updated_at, datetime)

    def test_str_method(self):
        """ str test """
        my_model = BaseModel()
        str_representation = f"[BaseModel] ({my_base.id}) {my_base.__dict__}"
        self.assertEqual(str(my_base), str_representation)

    def test_save_method(self):
        """ save test """
        my_base = BaseModel()
        prev_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(my_base.updated_at, prev_updated_at)

     def test_to_dict_method(self):
         """  to dict test """
        my_base = BaseModel()
        my_base.name = "My First Model"
        my_base.my_number = 89
        my_base_json = my_base.to_dict()
        self.assertIsInstance(my_base_json, dict)
        self.assertEqual(my_base_json['__class__'], 'BaseModel')
        self.assertEqual(my_base_json['name'], "My First Model")
        self.assertEqual(my_base_json['my_number'], 89)
        self.assertIsInstance(datetime.strptime(my_base_json['created_at'], "%Y-%m-%dT%H:%M:%S.%f"),
                              datetime)
        self.assertIsInstance(datetime.strptime(my_base_json['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"),
                              datetime)

    def test_to_dict_with_custom_attrs(self):
        """ test """
        my_base = BaseModel()
        my_base.custom_attr = "Custom Value"
        my_base_json = my_base.to_dict()
        self.assertEqual(my_base_json['custom_attr'], "Custom Value")

    def test_from_dict_to_instance(self):
        """ test """
        my_base = BaseModel()
        my_base.name = "My First Model"
        my_base.my_number = 89
        my_base_json = my_model.to_dict()
        new_model = BaseModel(**my_base_json)
        self.assertEqual(my_base.id, new_model.id)
        self.assertEqual(my_base.name, new_model.name)
        self.assertEqual(my_base.my_number, new_model.my_number)
        self.assertEqual(my_base.created_at, new_model.created_at)
        self.assertEqual(my_base.updated_at, new_model.updated_at)
        
    if __name__ == '__main__':
        nittest.main()
