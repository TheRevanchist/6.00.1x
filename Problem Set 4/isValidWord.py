def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    myHand = hand.copy()    
    for letter in word:
        if letter not in hand or myHand[letter] <= 0:
            return False
        else:
            myHand[letter] -= 1            
    if word not in wordList:
        return False
    else:
        return True         
   
            