#!/usr/bin/python3
""" file storage test """
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ file storage calss """

    def setUp(self):
        """ set up test """
        self.file_path = "file.json"
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.base_model.name = "TestModel"
        self.base_model.my_number = 42

    def tearDown(self):
        """ test """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_save_reload(self):
        """ test """
        self.base_model.save()
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertTrue(isinstance(all_objs, dict))
        self.assertIn(self.base_model.__class__.__name__ + "." + self.base_model.id, all_objs)
        reloaded_model = all_objs[self.base_model.__class__.__name__ + "." + self.base_model.id]
        self.assertEqual(reloaded_model.id, self.base_model.id)
        self.assertEqual(reloaded_model.name, self.base_model.name)
        self.assertEqual(reloaded_model.my_number, self.base_model.my_number)

if __name__ == "__main__":
    unittest.main()
