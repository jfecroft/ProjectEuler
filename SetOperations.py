from itertools import chain, combinations


def powerset(iterable):
    """
    return the powerset of *iterable*
    """
    xs = list(iterable)
    return list(chain.from_iterable(combinations(xs, n) for
                n in range(len(xs) + 1)))
