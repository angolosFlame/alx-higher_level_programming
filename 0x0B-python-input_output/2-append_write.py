#!/usr/bin/python3
"""
A function that appends a string at the end of a text file (UTF8) and returns the number of characters added:
Prototype: def append_write(filename="", text=""):
If the file doesn’t exist, it should be created
The with statement is being used
No need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module
"""

def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.

    args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The no characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
