def duplicate_encode(word):
    """
    The goal of this challenge is to convert a string to a
    new string where each character in the new string is "("
    if that character appears only once in the original string,
    or ")" if that character appears more than once in the original string.
    Ignore capitalization when determining if a character is a duplicate.
    """
    word = word.lower()
    wordlist = list(word)
    wordaux = []
    j = 0
    for i in wordlist:
        counter = wordlist.count(i,)
        if counter == 1:
            indice = wordlist.index(i)
            wordaux.insert(indice, '(')
            j += 1
        else:
            indice = wordlist.index(i, j)
            wordaux.insert(indice, ')')
            j += 1
    wordaux = ''.join(wordaux)
    return wordaux


print(duplicate_encode("Hello world"))