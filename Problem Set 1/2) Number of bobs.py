# Paste your code into this box 
s = 'abobobodhskbobob'
bob = 0
gjatesia = len(s)
for i in range(gjatesia-2):
    if s[i] == 'b':
        if s[i+1] == 'o':
            if s[i+2] == 'b':
                bob += 1
                 
print 'Number of times bob occurs is: ' + str(bob)                
             
         
 