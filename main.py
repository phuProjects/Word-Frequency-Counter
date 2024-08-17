import re


def word_freq_counter(file_name):


    with open(file_name) as file:
        text = file.read()


    #Make all words lowercase
    text = text.lower()

    #removes all punctation with the pattern [^\w\s]. Make sure the r is before the pattern, indicating that it is a raw string.
    text = re.sub(r'[^\w\s]', '', text)

    #create dict to store frequency of words. 
    word = {}


    return text
print(word_freq_counter('test.txt'))
