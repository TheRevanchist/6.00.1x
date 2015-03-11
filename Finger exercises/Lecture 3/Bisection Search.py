# Paste your code into this box
print 'Please think of a number between 0 and 100!'
secret = 82
low = 0
high = 100
guess = (low + high)/2
found = True 

while found == True:
    print 'Is your secret number ' + str(guess) + ' ?'
    answer = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if answer == 'l':
        low = guess
        guess = (low + high)/2
    elif answer == 'h':
        high = guess
        guess = (low + high)/2
    elif answer == 'c':
        print 'Game over. Your secret number was: ' + str(guess)
        found = False
    else:
        print 'Sorry, I did not understand your input.'  
        
                              
    
    
    