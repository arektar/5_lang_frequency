import collections
import re


def load_data(file_path):
    with open(file_path) as file:
        text = file.read()
    return text


def get_most_frequent_words(words):
    lot_of_freq_words = 10
    return collections.Counter(words).most_common(lot_of_freq_words)


def take_words(text):
    words = re.findall(r'\w+', text.lower())
    return words

if __name__ == '__main__':
    my_file_name = input("Write full file way: ")
    my_text = load_data(my_file_name)
    my_text_words = take_words(my_text)
    print("Топ часто встречающихся слов:")
    for fr_word, times_found in get_most_frequent_words(my_text_words):
        print("%s %d раз(а)." % (fr_word, times_found))
