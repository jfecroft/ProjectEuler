from numpy import binary_repr
from palindrome import is_palindrome

MAX_NUMBER = 1000000
sum_ = 0
palindromes = []

# Check to see if palindrome in base10.
for number in xrange(MAX_NUMBER+1):
    if is_palindrome(str(number)):
        palindromes.append(number)

# If palindrome in base10 see if also palindrome in base2.
for number in palindromes:
    if is_palindrome(binary_repr(number)):
        sum_ += number

print sum_
