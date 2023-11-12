#!/usr/bin/python3
"""some docs goes here"""
class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        """some docs goes here"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    
