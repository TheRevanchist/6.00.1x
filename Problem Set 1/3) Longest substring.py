# Paste your code into this box 
s = 'xbvxokvggii'
string1 = ''
string2 = ''

for i in s:
    if len(string2) == 0:
        string2 += i            
    elif i >= string2[-1]:
        string2 += i
        if len(string2) > len(string1):
            string1 = string2
    elif len(string2) > len(string1):
        string1 = string2
        string2 = i
    else:
         string2 = i
           
print 'Longest substring in alphabetical order is: ' + string1