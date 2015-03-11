def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    length = len(aStr)
    mid = len(aStr)/2
    
    if length == 0:
        return False
    elif length == 1:  
        if char == aStr:
            return True
        else:
            return False
    else:        
        if char == aStr[mid]:
            return True
        elif char < aStr[mid]:
            return isIn(char, aStr[0:mid])
        else:
            return isIn(char, aStr[mid+1:length])  
                                                            
    