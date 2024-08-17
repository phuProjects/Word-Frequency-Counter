import re


def word_freq_counter(file_name, the_word):

    with open(file_name) as file:
        text = file.read()

    #Make all words lowercase
    text = text.lower()

    #removes all punctation with the pattern [^\w\s]. Make sure the r is before the pattern, indicating that it is a raw string.
    text = re.sub(r'[^\w\s]', '', text)

    #split the text into words
    words = text.split()

    #create dict to store frequency of words. 
    word_count = {the_word: 0}

    for word in words:
        if word == the_word:
            word_count[the_word] += 1

    if word_count[the_word] >= 1:
        print(f"{the_word}: {word_count[the_word]}")
    else:
        print("The word you are looking here is NOT in here.")
    print("")

    return text
print(word_freq_counter('test.txt', "the"))
