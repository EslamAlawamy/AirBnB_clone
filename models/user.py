#!/usr/bin/python3
""" User model """
from models.base_model import BaseModel


class User(BaseModel):
    """represent User class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

def __init__(self, *args, **kwargs):
    """ Initialize a new User instance. """
    super().__init__(*args, **kwargs)
