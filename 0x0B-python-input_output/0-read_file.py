#!/usr/bin/python3
"""
A function that reads a text file (UTF8) and prints it to stdout:
Prototype: def read_file(filename=""):
The with statement is used in this function
No need to manage file permission or file doesn't exist exceptions.
"""

def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
