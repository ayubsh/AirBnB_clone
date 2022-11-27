#!/usr/bin/python3
""" User Module """
from models.base_model import BaseModel


class User(BaseModel):
    """ model for user classs """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
