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


    if __name__ == '__main__':
        nittest.main()
