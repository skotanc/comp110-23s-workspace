"""EX05 - 'list' Utility Functions."""
__author__ = "730551547"


def only_evens(numberlist: list[int]) -> list[int]:
    """Makes lists of even numbers."""
    evenlist = []
    for idx in numberlist:
        if ((idx % 2) == 0):
            evenlist.append(idx)
    return evenlist


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Contains the other two lists."""
    combinedlist = []
    for idx1 in list1:
        combinedlist.append(idx1)
    for idx2 in list2:
        combinedlist.append(idx2)
    return combinedlist


def sub(a_list: list[int], sindex: int, eindex: int) -> list[int]:
    """Puts a range of a list from start and end."""
    newlist = []
    if sindex < 0:
        sindex = 0
    if eindex >= len(a_list):
        eindex = len(a_list)
    if (sindex == eindex):
        return []
    for idx3 in range(sindex, eindex):
        if (sindex < eindex):
            newlist.append(a_list[idx3])
    return newlist