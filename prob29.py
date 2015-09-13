"""
solve problem 29
"""
import itertools


def distinct_terms(arange, brange):
    """
    distaict terms for a**b
    """
    distinctterms = set()
    for aaa, bbb in itertools.product(arange, brange):
        distinctterms.add(aaa**bbb)
    return distinctterms

print len(distinct_terms(range(2, 101), range(2, 101)))
