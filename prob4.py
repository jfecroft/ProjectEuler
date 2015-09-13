"""
Solves project euler problem 4.
"""
from itertools import product
from utils import is_palindrome

MAX = 999
HIGHEST = 0
for num1, num2 in product(range(MAX+1), range(MAX+1)):
    if is_palindrome(str(num1*num2)) and num1*num2 > HIGHEST:
        HIGHEST = num1*num2

print HIGHEST
