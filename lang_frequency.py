import collections

def load_data(filepath):
    with open(filepath) as file:
        text=file.read()
    return text

def get_most_frequent_words(text):
    freq_collection_list=collections.Counter()
    words=text.split()
    for word in words:
        freq_collection_list[word]+=1
    return freq_collection_list

if __name__ == '__main__':
    file_name=input("Write full file name: ")
    text=load_data(file_name)
    most_oft_words=get_most_frequent_words(text)
    print("Топ часто встречающихся слов:")
    for word,times_found in most_oft_words.most_common(10):print(word+" "+str(times_found)+" раз(а).")
