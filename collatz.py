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
