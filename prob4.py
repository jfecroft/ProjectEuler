"""Solves project euler problem 4."""
from itertools import product
from Palindrome import is_palindrome

MAX = 999
highest = 0
for num1, num2 in product(range(MAX+1), range(MAX+1)):
    if is_palindrome(str(num1*num2)) and num1*num2 > highest:
        highest = num1*num2

print highest
