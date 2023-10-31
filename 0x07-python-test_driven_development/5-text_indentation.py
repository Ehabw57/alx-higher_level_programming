#!/usr/bin/python3
"""
one modlue for one fuctiuon
"""


def text_indentation(text):
    """
    Adds a new line after each . and ? and : in a
    sample string

    Args:
    text (str): The sample string to replace

    Rasies : TypeError if text is not a str
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in [".", "?", ":"]:
            print("\n")
            while text[i + 1] == " ":
                i += 1
        i += 1
