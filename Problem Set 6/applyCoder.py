def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO
    myString = ''
    for letter in text:
        if letter.isalpha() == True:
            myString += coder[str(letter)]
        else:
            myString += letter
    return myString     