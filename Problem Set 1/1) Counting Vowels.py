s = 'asashduheioudhsjd'
vowels = 0
iterate = len(s)
for i in range(iterate):
    if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
        vowels += 1
        
print 'Number of vowels: ' + str(vowels)        