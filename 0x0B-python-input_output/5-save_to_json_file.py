#!/usr/bin/python3
import json as JSON

"""module for saving objects as json data"""


def save_to_json_file(my_obj, filename):
    """
    Saves objects to a json file

    Args:
        filename (str): Name of json file to save data in
        my_obj (any): Object to be saved
    """
    with open(filename, "w") as file:
        JSON.dump(my_obj, file)
