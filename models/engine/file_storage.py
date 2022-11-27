#!/usr/bin/python3
"""File storage module """
import json
import os.path


class FileStorage:
    """ storage class that serializes instances to a
    JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        self.__objects[obj.__class__.__name__ + '.' + str(obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        with open(self.__file_path, 'w') as file:
            d = {k: o.to_dict() for k, o in self.__objects.items()}
            json.dump(d, file)

    def reload(self):
        """ deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as file:
                ld = json.load(file)
                for k, v in ld.items():
                    self.__objects[k] = eval(v['__class__'])(**v)
        else:
            return
