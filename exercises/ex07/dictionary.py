"""EX07 - Dictionary Functions."""
__author__ = "730551547"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts a dictionary."""
    keylist: list[str] = []
    valuelist: list[str] = []
    for x in input:
        keylist.append(x)
        valuelist.append(input[x])
    completedict: dict[str, str] = {}
    length: int = len(keylist)
    for i in range(length):
        completedict[valuelist[i]] = keylist[i]
    return completedict


def favorite_color(input: dict[str, str]) -> str:
    """Outputs the most common favorite color."""
    colorlist: list[str] = []
    for x in input:
        colorlist.append(input[x])
    mostcount: int = 0
    for y in range(len(colorlist)):
        count: int = 1
        for z in range(y + 1, len(colorlist)):
            if colorlist[y] == colorlist[z]:
                count = count + 1
        if count > mostcount:
            mostcount = count
            mostcommon = colorlist[y]
    return mostcommon


def count(input: list[str]) -> dict[str, int]:
    """Counts the number of values in a list."""
    newdict: dict[str, int] = {}
    for x in input:
        if (x in newdict):
            newdict[x] += 1
        else:
            newdict[x] = 1
    return newdict
