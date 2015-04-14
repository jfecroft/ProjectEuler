"""
solve problem 39
"""
from operator import itemgetter


def integer_right_triangles(perimeter):
    """
    return right angle triangles with integer side and perimeter
    """
    count = 0
    for aaa in xrange(1, perimeter/2+1):
        for bbb in xrange(aaa+1, perimeter-aaa):
            ccc = perimeter - aaa - bbb
            if aaa**2 + bbb**2 == ccc**2:
                count += 1
    return count

MAXIMUM = max(
    ((i, integer_right_triangles(i)) for i in xrange(1001)),
    key=itemgetter(1)
)
print MAXIMUM[0]
