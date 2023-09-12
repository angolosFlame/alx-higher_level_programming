#!/usr/bin/python3
"""
A function that returns an object (Python data structure) represented by a JSON string:
Prototype: def from_json_string(my_str):
No  need to manage exceptions if the JSON string doesn’t represent an object.
"""
import json

def from_json_string(my_str):
    return json.loads(my_str)
