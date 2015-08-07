"""
project euler utils
"""


def is_palindrome(string):
    """ Return if a string is a palindrome."""

    if not isinstance(string, str):
        string = str(string)
    if len(string) == 1:
        return True
    elif string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return False
