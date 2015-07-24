from functools import wraps


def memoize(func):
    """
    decortor for cacheing 
    """
    # Everything here happens when the decorator LOADS and wrapper
    # has access to it.
    # TODO add argument cache last x calls.
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Things here happen each time the final wrapped function gets CALLED
        key = args + tuple(kwargs.items())
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

@memoize
def collatz(num):
    """
    return the collatz path for number
    """
    collatz_list = [num]
    if num == 1:
        pass
    elif num % 2 == 0:
        collatz_list.extend(collatz(num/2))
    else:
        collatz_list.extend(collatz(3*num+1))
    return collatz_list

def find_in_list_of_lists(data, search):
    """
    find *search* in list of lists *data*
    """
    #  should in general be recursive
    for sublist in data:
        if search in sublist:
            return sublist
