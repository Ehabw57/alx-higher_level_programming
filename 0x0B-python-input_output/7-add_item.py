#!/usr/bin/python3
"""Creat a json file with list of argumnts passed"""
from sys import argv

save_json = __import__("5-save_to_json_file").save_to_json_file
load_json = __import__("6-load_from_json_file").load_from_json_file

try:
    mylist = load_json('add_item.json')
except FileNotFoundError:
    mylist = []
    save_json(mylist, 'add_item.json')

mylist.extend(argv[1:])
save_json(mylist, 'add_item.json')
