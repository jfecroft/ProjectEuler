"""
project euler utils
"""


def open_file(filen):
    """
    open file and return lines
    """
    with open(filen) as ofile:
        lines = ofile.readlines()
    return lines


def is_palindrome(string):
    """ Return if a string is a palindrome."""

    if not isinstance(string, str):
        string = str(string)
    if len(string) in (1, 0):
        return True
    elif string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return False
