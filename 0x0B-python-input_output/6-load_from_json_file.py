#!/usr/bin/python3
"""module for saving objects as json data"""
import json as JSON


def load_from_json_file(filename):
    """
    loads objects from a json file

    Args:
        filename (str): Name of json file to load data from

    """
    with open(filename, "r") as file:
        return JSON.load(file)
