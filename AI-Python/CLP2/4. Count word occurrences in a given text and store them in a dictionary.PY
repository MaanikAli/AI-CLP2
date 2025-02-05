def count_word_occurrences(text):
    # Split the text into words
    words = text.split()
    # Create an empty dictionary to store word counts
    word_counts = {}
    # Iterate over each word in the list
    for word in words:
        # Convert the word to lowercase to ensure case-insensitive counting
        word = word.lower()
        # Increment the count for the word in the dictionary
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

# Example usage
text = "This is a sample text with several words. This text is a sample text."
word_counts = count_word_occurrences(text)
print(word_counts)