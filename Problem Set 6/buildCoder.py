def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO 
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    myDict = {}

    for i in range(len(upper)):
        myDict[upper[i]] = upper[(i + shift) % 26]
    for i in range(len(lower)):
        myDict[lower[i]] = lower[(i + shift) % 26]   
    return myDict
              
                  
    
        

    