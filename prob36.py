from numpy import binary_repr
from Palindrome import IsPalindrome

NumMax = 1000000
Sum = 0
for Num in xrange(NumMax):
 if IsPalindrome(str(Num)) and IsPalindrome(binary_repr(Num)):
  Sum += Num

print Sum
