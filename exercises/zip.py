def zip(strings: list[str], integers: list[int]) -> dict[str,int]:
    """A function that takes in strings and integers and returns a dict with the first part are the keys and the values are the second part"""
    emptydict = {}
    if (len(strings) == 0 or len(integers)== 0 or (len(strings)) != len(integers)):
        return emptydict
    completedict = {}
    length = int(len(strings))
    for x in range(length):
        completedict[strings[x]] = integers [x]
    return completedict
