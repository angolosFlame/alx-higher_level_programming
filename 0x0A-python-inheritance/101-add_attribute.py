#!/usr/bin/python3
"""A function that adds a new attribute to an object if it’s possible:
Raise a TypeError exception, with the message can't add new attribute if the object can’t have new attribute
Not allowed to use try/except
Not allowed to import any module"""

def add_attribute(obj, att, value):
    """Statement to add a new attribute to an object if possible.

    Args:
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute to add to obj.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
