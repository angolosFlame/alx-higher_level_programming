#!/usr/bin/python3
"""
A function that writes an Object to a text file, using a JSON representation:
Prototype: def save_to_json_file(my_obj, filename):
usage of the with statement
No need to manage exceptions if the object can’t be serialized.
No need to manage file permission exceptions.
"""
import json

def save_to_json_file(my_obj, filename):
    with open(filename, "w") as f:
        json.dump(my_obj, f)
