#!/usr/bin/python3
"""
Base module
"""


import json

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None and isinstance(id, int):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):

        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)


    def from_json_string(json_string):

        if json_string is None:
            json_string = []    
        return json.loads(json_string)


    def save_to_file(cls, list_objs):

        new_list = []

        if list_objs is None:
            f = cls.to_json_string(new_list)
        
        filename = "{}.json".format(cls.__name__)

        with open(filename, "w") as fp:
            fp.write(list_objs)


    def create(cls, **dictionary):

        if cls.__name__ is "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ is "Square":
            new = cls(1)
        
        new.update(**dictionary)

        return new

    
    def load_from_file(cls):

        filename = "{}.json".format(cls.__name__)