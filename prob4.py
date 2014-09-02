import itertools


def IsPalindrome(String):
 ReversedString = String[::-1]
 if String == ReversedString: return True
 return False

NumMax = 999
Highest = 0
for i,j in itertools.product(range(NumMax+1),range(NumMax+1)):
 if IsPalindrome(str(i*j)) and i*j > Highest:
  Highest = i*j


print Highest
