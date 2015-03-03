def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    bestShift = 0
    wordsCount = 0
    for shift in range(0, 26):
        wordsCountTemp = 0
        decodedText = applyShift(text, shift)
        splitText = decodedText.split(' ')
        for word in splitText:
            if isWord(wordList, word):
                wordsCountTemp += 1
        if wordsCountTemp > wordsCount:
            wordsCount = wordsCountTemp
            bestShift = shift
    return bestShift 