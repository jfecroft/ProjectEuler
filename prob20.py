from math import factorial
digitstring = str(factorial(100))
print sum((int(digitstring[i]) for i in range(len(digitstring))))
