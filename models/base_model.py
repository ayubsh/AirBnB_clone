#!/usr/bin/python3
""" Base model module """
import uuid
import datetime
from models import storage


class BaseModel:
    """ base class that defines
        all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """ constructor for the baseclass model """
        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                elif k == 'updated_at':
                    v = datetime.datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                elif k == 'created_at':
                    v = datetime.datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if 'id' not in kwargs.keys():
                    self.id = str(uuid.uuid4())
                if 'created_at' not in kwargs.keys():
                    self.created_at = datetime.datetime.now()
                if 'updated_at' not in kwargs.keys():
                    self.updated_at = datetime.datetime.now()
                setattr(self, k, v)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """ prints the class in
            [<class name>] (<self.id>) <self.__dict__>
        """
        s = ("[{}] ({}) {}".format(self.__class__.__name__,
                                   self.id, self.__dict__))
        return s

    def save(self):
        """ updates the public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """ returns dictionary containing all keys/values of __dict__ of
            the instance
        """
        d = self.__dict__.copy()
        d['__class__'] = self.__class__.__name__
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        return d
