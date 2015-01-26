import itertools

LowLim = 2
UpLim = 100

A = range(LowLim, UpLim+1)
B = range(LowLim, UpLim+1)

DistinctTerms = set()
for a, b in itertools.product(A, B):
    DistinctTerms.add(a**b)

print len(DistinctTerms)
