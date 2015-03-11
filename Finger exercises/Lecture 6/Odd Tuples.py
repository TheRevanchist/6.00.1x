def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    length = len(aTup)
    tup = ()
    for element in range(length):
        if element % 2 == 0:
            tup = tup + (aTup[element],)
    return tup        
    