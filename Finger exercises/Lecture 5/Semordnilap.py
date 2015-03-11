def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    # Your code here
    length1 = len(str1)
    length2 = len(str2)
    
    if length1 != length2:
        return False
    
    elif length1 == 1:
        if str1 == str2:
            return True
        else:
            return False            
    elif str1[0] == str2[-1]:
        return semordnilap(str1[1:], str2[:-1])
    else:
        return False       