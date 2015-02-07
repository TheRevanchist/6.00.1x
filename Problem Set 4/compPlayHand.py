def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    score = 0
    
    while calculateHandlen(hand) > 0: 
                
        # Display the hand
        print 'Current Hand: ', 
        displayHand(hand)
        word = compChooseWord(hand, wordList, n)
        if word != None:
            wordScore = getWordScore(word, n)
            score += wordScore
            print '"%s" earned %d points. Total: %d points' % (word, wordScore, score)
            print ''
            hand = updateHand(hand, word)
        else:
            break

    print 'Total score: ' + str(score) + ' points'    
                    
                  