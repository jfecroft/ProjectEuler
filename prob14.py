"""
solutions to problem 14
"""


def find_in_list_of_lists(data, search):
    """
    find *search* in list of lists *data*
    """
    #  should in general be recursive
    for sublist in data:
        if search in sublist:
            return sublist


def collatz(num, collatz_list=None, already_computed=None):
    """
    return the collatz path for number
    """
    if collatz_list is None:
        collatz_list = []
    if already_computed is None:
        already_computed = [[]]
    collatz_list.append(num)
    known_path = find_in_list_of_lists(already_computed, num)
    if known_path is not None:
        collatz_list.extend(known_path[known_path.index(num)+1:])
        already_computed.remove(known_path)
        already_computed.append(collatz_list)
        return collatz_list
    if num == 1:
        return collatz_list
    if num % 2 == 0:
        return collatz(num/2, collatz_list)
    else:
        return collatz(3*num+1, collatz_list)


MAX = 0
MAX_NUM = 1000000
for i in xrange(2, MAX_NUM):
    CollatzList = collatz(i, None)
    length = len(CollatzList)
    if length > MAX:
        Max = length
        StartNum = CollatzList[0]

print StartNum, Max
