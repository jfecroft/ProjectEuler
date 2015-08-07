from fractions import Fraction

def solution(denom, num):
    return (Fraction(1, denom) - Fraction(1, num)).numerator == 1


def num_sols(num):
    total = 0
    for i in xrange(num+1, num*2+1):
        total += solution(num, i)
    return total


i = 1
while num_sols(i) < 10000:
    i += 1
    print i

# works but slow
print num_sols(180180) 
    
