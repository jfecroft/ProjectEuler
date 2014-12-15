from numpy import binary_repr
from Palindrome import is_palindrome

NumMax = 1000000
Sum = 0
palindromes = []

# Check to see if palindrome in base10.
for Num in xrange(NumMax):
    if is_palindrome(str(Num)):
        palindromes.append(Num)

# If palindrome in base10 see if also palindrome in base2.
for Num in  palindromes:
    if is_palindrome(binary_repr(Num)):
        Sum += Num

print Sum
