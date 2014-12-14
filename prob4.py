from itertools import product
from Palindrome import is_palindrome

MAX = 999
highest = 0
for i, j in product(range(MAX+1), range(MAX+1)):
 if is_palindrome(str(i*j)) and i*j > highest:
  highest = i*j

print highest
