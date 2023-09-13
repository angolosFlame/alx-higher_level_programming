#!/usr/bin/python3
"""A class MyInt that inherits from int"""

class MyInt(int):
    """Statemnet of the class MyInt"""

    def __eq__(self, value):
        """defines the behaviour of the value object."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
