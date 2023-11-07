#!/usr/bin/python3
"""Module of class Student"""


class Student:
    def __init__(self, firstname, lastname, age):
        """instliase a new student instance"""
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

        def to_json(self):
            """Rreturns the dictionary with simple data structure"""
            return self.__dict__
