def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

testList = [1, -4, 8, -9]

# Your Code Here                
def absolute(a):
    return abs(a)
    
applyToEach(testList, absolute)    

# Your Code Here
def plusOne(a):
    return a + 1
    
applyToEach(testList, plusOne)  

                
# Your Code Here
def square(a):
    return a * a
    
applyToEach(testList, square)    
                                                