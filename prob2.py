"""
solve problem 2
"""
TOTAL = 0
NUM1, NUM2 = 0, 1
UPPER_LIMIT = 4000000
while NUM2 < UPPER_LIMIT:
    NUM1, NUM2 = NUM2, NUM1+NUM2
    if NUM2 % 2 == 0:
        TOTAL += NUM2

print TOTAL
