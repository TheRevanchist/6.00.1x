def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    story = getStoryString()
    shift = findBestShift(wordList, story)
    decryptedStory = applyShift(story, shift)
    return decryptedStory
    # story for Jack Florey, a mythical hacker who was a failure