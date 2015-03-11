def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    a = 0
    b = 0
    for value in aDict:
        b = aDict[value]
        b = len(b)
        a += b
    return a    
