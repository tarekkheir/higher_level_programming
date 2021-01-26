#!/usr/bin/python3
"""
Base module
"""


import json


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init execution"""
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

    @staticmethod
    def from_json_string(json_string):

        if json_string is None:
            json_string = []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):

        new_list = []
        filename = "{}.json".format(cls.__name__)

        for i in list_objs:
            new_list.append(i.to_dictionary())

        data = cls.to_json_string(new_list)

        with open(filename, "w") as fp:
            fp.write(data)

    @classmethod
    def create(cls, **dictionary):

        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)

        new.update(**dictionary)

        return new

    @classmethod
    def load_from_file(cls):

        filename = "{}.json".format(cls.__name__)
        new_list = []

        try:
            with open(filename, "r") as f:
                data = f.read()
            new_list = cls.from_json_string(data)

            for i in range(0, len(new_list)):
                new_list[i] = cls.create(**new_list)
        except FileNotFoundError:
            pass
        return new_list
