#!/usr/bin/python3
""" Base model module """
import uuid
import datetime

class BaseModel:
    """ base class that defines 
        all common attributes/methods for other classes
    """
    def __init__(self):
        """ constructor for the baseclass model """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ prints the class in 
            [<class name>] (<self.id>) <self.__dict__>
        """
        s = ("[{}] ({}) {}".format(self.__class__.__name__,self.id, self.__dict__))
        return s

    def save(self):
        """ updates the public instance attribute updated_at 
            with the current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ returns dictionary containing all keys/values of __dict__ of 
            the instance
        """
        d = self.__dict__
        d['__class__'] = self.__class__.__name__
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        return d
