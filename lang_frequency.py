def load_data(filepath):
    file=open(filepath)
    text=file.read()
    return text

def get_most_frequent_words(text):
    words=text.split()
    frequancy={}
    for word in words:
        try: frequancy[word]+=1
        except:frequancy[word]=1
    for i in range(10):
        max_fr_word=['',0]
        for word in list(frequancy):
            if frequancy[word]>max_fr_word[1]:
                max_fr_word[0]=word
                max_fr_word[1]=frequancy[word]
        print(max_fr_word[0])
        frequancy.pop(max_fr_word[0])

if __name__ == '__main__':
    name=input("Write full file name: ")
    text=load_data(name)
    get_most_frequent_words(text)
