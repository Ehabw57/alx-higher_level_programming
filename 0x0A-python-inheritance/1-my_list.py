#!/usr/bin/python3
"""moudle of my list class"""


class MyList(list):
    """chiled class of list"""

    def print_sorted(self):
        print("{}".format(sorted(self)))
