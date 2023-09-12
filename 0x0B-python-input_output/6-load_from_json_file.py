#!/usr/bin/python3
"""
A function that creates an Object from a “JSON file”:
Prototype: def load_from_json_file(filename)
Usage of the with statement
No need to manage exceptions if the JSON string doesn’t represent an object.
No need to manage file permissions / exceptions.
"""
import json

def load_from_json_file(filename):
    with open(filename) as f:
        return json.load(f)
