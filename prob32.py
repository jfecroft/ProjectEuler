"""
solve project euler problem 32
"""

import itertools
CALC = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
PANDIGITAL = set()
for combination in itertools.permutations(CALC, len(CALC)):
    comb = list(combination)
    for i in range(1, len(combination)):
        for j in range(i+1, len(combination)):
            a = int(''.join(comb[0:i]))
            b = int(''.join(comb[i:j]))
            c = int(''.join(comb[j:]))
            if a*b == c and a < b:
                PANDIGITAL.add(c)

print sum(PANDIGITAL)
