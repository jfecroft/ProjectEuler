"""
solve problem 29
"""
import itertools

LOWLIM = 2
UPLIM = 100

A = range(LOWLIM, UPLIM+1)
B = range(LOWLIM, UPLIM+1)

DISTINCTTERMS = set()
for a, b in itertools.product(A, B):
    DISTINCTTERMS.add(a**b)

print len(DISTINCTTERMS)
