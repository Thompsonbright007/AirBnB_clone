#!/usr/bin/python3
<<<<<<< HEAD
""" Module holds classes for managing data storage """
import json
from os import path
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }


class FileStorage():
    """
        handles serialization and deserialization of object
        dictionaries to json and saves them to file
        Attributes:
            file_path (str): path of the file for saving object data
            objects (dict): private dictionary record of all objects in storage
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """
            gives access to the objects attribute
            which holds all data stored by the app
=======
"""
Defines a File storage class that serializes instances to JSON file and
    "deserializes JSON file to instances
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Represents an instance of the FileStorage class

    Attributes: 
        __file_path: A path to the JSON file
        __objects: A dict to store all objects
    """
    __file_path = 'file.json'
    __objects = {}


    def all(self):
        """
        returns a dictionary __objects
>>>>>>> 2aa933593cb0d02a51579735a0b9d2f24b156cba
        """
        return FileStorage.__objects

    def new(self, obj):
        """
<<<<<<< HEAD
            Method stores a newly created object into
            the objects dictionary
            Params:
                obj (BaseModel): the the new object to store
        """
        FileStorage.__objects[obj.__class__.__name__+"."+obj.id] = obj

    def save(self):
        """ Method writes all objects data into a json file"""
        with open(FileStorage.__file_path, 'w') as fl:
            serializable = {}
            for key, val in FileStorage.__objects.items():
                serializable[key] = val.to_dict()
            json.dump(serializable, fl)

    def reload(self):
        """
            Loads and reads stored data from a json file
            and stores into objects dictionaty
        """
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as fl:
                temp_objects = json.load(fl)
                for key, value in temp_objects.items():
                    cls = classes[key.split(".")[0]]
                    FileStorage.__objects[key] = cls(**value)
=======
        sets in __objects the obj with key <obj class name>.id
        
        Args:
            obj: object to set to __object
        """
        key = obj.__class__.__name__ + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        new_dict = {}
        for key, obj in FileStorage.__objects.items():
            new_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as new_file:
            new_file.write(json.dumps(new_dict))

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; 

        Raises:
            an exception If the file doesn’t exist
        """
        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                }
        try:
            with open(FileStorage.__file_path, "r") as loaded_f:
                fetched_dicts = json.load(loaded_f)
                for key, obj in fetched_dicts.items():
                    self.all()[key] = classes[obj['__class__']](**obj)
        except FileNotFoundError:
             return
>>>>>>> 2aa933593cb0d02a51579735a0b9d2f24b156cba
