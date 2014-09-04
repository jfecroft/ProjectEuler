from numpy import binary_repr
from Palindrome import IsPalindrome

NumMax = 1000000
Sum = 0
PalindromesInBase2=[]
#check to see if palindrome in base10
for Num in xrange(NumMax):
 if IsPalindrome(str(Num)):
  PalindromesInBase2.append(Num)

#if palindrome in base 2 see if also palindrome in base2
for Num in  PalindromesInBase2:
 if IsPalindrome(binary_repr(Num)):
  Sum += Num

print Sum
