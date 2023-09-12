#!/usr/bin/python3
"""
A function that returns the JSON representation of an object (string):
Prototype: def to_json_string(my_obj):
No  need to manage exceptions if the object can’t be serialized.
"""

import json

def to_json_string(my_obj):
    return json.dumps(my_obj)
