"""
solve problem 48
"""
SUM = 0
for i in xrange(1, 1001):
    SUM += i**i

print str(SUM)[-10:]
