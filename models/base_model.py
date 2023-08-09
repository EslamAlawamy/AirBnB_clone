#!/usr/bin/python3
""" all common attributes/methods for other classes """
import uuid
from datetime import datetime


class BaseModel:
    """ Base Model Class """
    def __init__(self):
        """ initialize the function """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ return string """
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        """ updates the public instance attribute """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing
        all keys/values of __dict__ of the instance
        """
        my_obj_dict = self.__dict__.copy()
        my_obj_dict["__class__"] = self.__class__.__name__
        my_obj_dict["created_at"] = self.created_at.isoformat()
        my_obj_dict["updated_at"] = self.updated_at.isoformat()
        return my_obj_dict
