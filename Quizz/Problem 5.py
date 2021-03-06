def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Your Code Here
    newString = ''
    i = 0
    while i < len(s1) and i < len(s2):
        newString += s1[i]
        newString += s2[i]
        i += 1
        
    newString += s1[i:] 
    newString += s2[i:]
    return newString
