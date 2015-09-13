"""
sove project euler problem 55
"""
from utils import is_palindrome
import sys


def lychrel_number(num, max_rec=50, rec=0):
    """
    return if is lychrel_number
    """
    if is_palindrome(num):
        return True
    elif rec >= max_rec:
        return False
    else:
        return lychrel_number(num + int(str(num)[::-1]), rec=rec+1)


def main():
    """
    execute from command line
    """
    total = 0
    for i in range(10000):
        total += not lychrel_number(i)
    print total

if __name__ == "__main__":
    sys.exit(main())
