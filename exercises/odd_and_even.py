def odd_and_even(numberlist: list[int]) -> (list[int]):
    numberlist = input("Enter a list of numbers: ")
    i = 0
    newlist = []
    for numberlist[i] in numberlist:
        if ((numberlist[i] % 1) == 0 and (i % 2) == 0):
            newlist.append(numberlist[i])
            i += 1
        else: 
            i +=1
    return newlist

