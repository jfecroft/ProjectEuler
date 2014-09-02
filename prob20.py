from math import factorial
digitstring = str(factorial(100))
digits = [int(digitstring[i]) for i in range(len(digitstring))]
print sum(digits)

