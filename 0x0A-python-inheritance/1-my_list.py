#!/usr/bin/python3
"""MyList section"""


class MyList(list):
    """MyList class, which Inherits from list"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
