#!/usr/bin/python3
"""Module of class Student"""


class Student:
    def __init__(self, firstname, lastname, age):
        """instliase a new student instance"""
        self.first_name = firstname
        self.last_name = lastname
        self.age = age

    def to_json(self, attrs=None):
        """Rreturns the dictionary with simple data structure"""
        if isinstance(attrs, list) and all(isinstance(e, str) for e in attrs):
            new = {K: self.__dict__[K] for K in self.__dict__.keys() & attrs}
            return new

        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the SELF"""
        for attr in json.keys():
            self.__dict__[attr] = json[attr]
