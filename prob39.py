from operator import itemgetter


def integer_right_triangles(perimeter):
    count = 0
    for a in xrange(1, perimeter/2+1):
        for b in xrange(a+1, perimeter-a):
            c = perimeter - a - b
            if a**2 + b**2 == c**2:
                count += 1
    return count

maximum = max(
    ((i, integer_right_triangles(i)) for i in xrange(1001)),
    key=itemgetter(1)
)
print maximum[0]
