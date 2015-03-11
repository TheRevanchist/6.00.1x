def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    
    minimum = min(a,b)  

    while minimum >= 1:
        if minimum == 1:
            return minimum
        elif (a % minimum) == 0 and (b % minimum) == 0:
            return minimum  
        minimum -= 1   
