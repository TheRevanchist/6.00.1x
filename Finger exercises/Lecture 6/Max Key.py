def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    
    maximum = None
    a = 0
    maxKey = None
    for key in aDict:
        a = aDict[key]
        a = len(a)
        if a > maximum:
            maxKey = key
            maximum = a
                
    return maxKey        
    