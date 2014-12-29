from operator import itemgetter


def recurrence_length(n):
    """
    Return the length of the recurrnce cycle for the decimal expansion of 1/*n*

    The multiplicative order of 10 mod an integer n relatively prime to 10
    gives the period of the decimal expansion of the reciprocal of n
    (Glaisher 1878, Lehmer 1941).
    http://mathworld.wolfram.com/MultiplicativeOrder.html
    """
    for length in xrange(1, n):
        if 1 == 10**length % n:
            return length
    return 0

maximum_recurrence = max(
    ((i, recurrence_length(i)) for i in xrange(1, 1001)),
    key=itemgetter(1)
)[0]
print maximum_recurrence
