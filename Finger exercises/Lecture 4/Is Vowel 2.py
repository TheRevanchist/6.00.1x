def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    # Your code here
    vowels = 'aAeEiIoOuU'
    a = char in vowels
    return a
