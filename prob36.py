"""
solve problem 36
"""
# pylint: disable-msg=E0611
from numpy import binary_repr
from palindrome import is_palindrome

MAX_NUMBER = 1000000
SUM = 0
PALINDROMES = []

# Check to see if palindrome in base10.
for number in xrange(MAX_NUMBER+1):
    if is_palindrome(str(number)):
        PALINDROMES.append(number)

# If palindrome in base10 see if also palindrome in base2.
for number in PALINDROMES:
    if is_palindrome(binary_repr(number)):
        SUM += number

print SUM
