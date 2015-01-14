def FindInListofLists(data, search):
    """
    find *search* in list of lists *data*
    """
    #  should in general be recursive
    for sublist in data:
        if search in sublist:
            return sublist


def collatz(n, CollatzList=None, AlreadyComputed=[[]]):
    #  AlreadyComputed is a mutable default will always update whenever used
    if CollatzList is None:
        CollatzList = []
    CollatzList.append(n)
    KnownPath = FindInListofLists(AlreadyComputed, n)
    if KnownPath is not None:
        CollatzList.extend(KnownPath[KnownPath.index(n)+1:])
        AlreadyComputed.remove(KnownPath)
        AlreadyComputed.append(CollatzList)
        return CollatzList
    if n == 1:
        return CollatzList
    if n % 2 == 0:
        return collatz(n/2, CollatzList)
    else:
        return collatz(3*n+1, CollatzList)


Max = 0
NumMax = 1000000
for i in xrange(2, NumMax):
    CollatzList = collatz(i, None)
    length = len(CollatzList)
    if length > Max:
        Max = length
        StartNum = CollatzList[0]

print StartNum, Max
