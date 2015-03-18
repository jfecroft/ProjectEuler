from itertools import chain, combinations


def powerset(iterable):
    """
    return the powerset of *iterable*
    """
    i_list = list(iterable)
    #  should return a set not a list
    return list(chain.from_iterable(combinations(i_list, n) for n in range(
        len(i_list) + 1)))
