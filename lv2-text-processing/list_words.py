def text_to_unique_words(text):
    # split the text into a list of words
    words = text.split()

    # create an empty list to hold the cleaned words
    clean_words = []

    # iterate over the words
    for word in words:
        # remove punctuation marks from the word
        word = ''.join(char for char in word if char not in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')

        # convert the word to lowercase
        word = word.lower()

        # add the cleaned word to the list of clean words
        clean_words.append(word)

    sorted_words = sorted(clean_words)

    result = []

    for w in sorted_words:
        if w not in result:
            result.append(w)

    return result


for x in text_to_unique_words("The apple doesn't fall far from the tree."):
    print(x)

