source_text = "ASDF is the sequence of letters that appear on the first four keys on the home row of a QWERTY or QWERTZ keyboard. They are often used as a sample or test case or as random, meaningless nonsense. It is also a common learning tool for keyboard classes, since all four keys are located on Home row." # from the wikipedia


# Function to count the number of letters in a string
def number_of_letters_in(text):
    # Initialize the count to zero
    count = 0

    # Loop through the string and count each letter
    for char in text:
        if char.isalpha():
            count += 1

    # Return the final count
    return count


# Function to count the number of words in a string
def number_of_words_in(text):
    # Use the split() method to split the string into a list of words
    words = text.split()

    # Return the length of the list of words
    return len(words)


def number_of_sentences_in(text):
    # Use the split() method to split the string into a list of words
    words = text.split('.')

    # Return the length of the list of words
    return len(words) - 1


# Function to calculate the average length of the words in a string
def average_word_length(text):
    # Use the split() method to split the string into a list of words
    words = text.split()

    # Calculate the total length of all words
    total_length = 0
    for word in words:
        total_length += len(word)

    # Calculate the average length of the words
    avg_length = total_length / len(words)

    # Return the average length
    return avg_length


