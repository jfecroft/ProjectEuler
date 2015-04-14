"""
solve problem 20
"""
from math import factorial
DIGITSTRING = str(factorial(100))
print sum((int(DIGITSTRING[i]) for i in range(len(DIGITSTRING))))
