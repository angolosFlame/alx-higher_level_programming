#!/usr/bin/python3
"""
A function that writes a string to a text file (UTF8) and returns the number of characters written:
Prototype: def write_file(filename="", text=""):
The with statement
No need to manage file permission exceptions.
The function creates the file if doesn’t exist.
The function overwrite the content of the file if it already exists.
You are not allowed to import any module
"""

def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
