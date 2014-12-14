MAX_NUMBER = 1000 

for a in xrange(1, MAX_NUMBER):
    for b in xrange(a, MAX_NUMBER-a+1):
        c = MAX_NUMBER-a-b
        if a**2 + b**2 == c**2:
            print a*b*c
