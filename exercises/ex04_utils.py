"""Ex04 - 'list' Utility Functions."""
__author__ = "730551547"


def all(integers: list[int], numbers: int) -> bool:
    """Given a list of ints, it says if all the ints are the same as given int."""
    order = 0
    if (len(integers) == 0):
        return False
    while (order < len(integers)):
        if (integers[order] == numbers):
            order = order + 1
            if (order == len(integers)):
                return True
        else:
            return False


def max(findmax: list[int]) -> int:
    """Finds the max of a list."""
    mymax = -1000000
    eachnum = 0
    if (len(findmax) == 0):
        raise ValueError("max() arg is an empty List")
    while (eachnum != len(findmax)):
        if (mymax < findmax[eachnum]):
            mymax = findmax[eachnum]
        eachnum = eachnum + 1
    return mymax


def is_equal(firstlist: list[int], secondlist: list[int]) -> bool:
    """Checks if the elements of two lists are equal."""
    first = 0
    second = 0
    if ((len(firstlist) == 0) and (len(secondlist) == 0)):
        return True
    if ((len(firstlist) == 0) and (len(secondlist) != 0)):
        return False
    if ((len(firstlist) != 0) and (len(secondlist) != 0)):
        return False
    while (first < len(firstlist) and second < len(secondlist)):
        if (firstlist[first] == secondlist[second]):
            first = first + 1
            second = second + 1
            if (first == len(firstlist) and second == len(secondlist)):
                return True
        else:
            return False  

    