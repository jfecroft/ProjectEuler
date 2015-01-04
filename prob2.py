sum = 0
a, b = 0, 1
UPPER_LIMIT = 4000000
while b < UPPER_LIMIT:
    a, b = b, a+b
    if b % 2 == 0:
        sum += b

print sum
