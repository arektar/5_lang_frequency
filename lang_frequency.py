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
    values=list(frequancy.values())
    values.sort()
    values.reverse()
    printnum=10

    for value in values:
        for key in frequancy.keys():
            if frequancy[key]==value:
                print(str(key))
                printnum-=1
            if printnum == 0:break
        if printnum==0:break

if __name__ == '__main__':
    name=input("Write full file name: ")
    text=load_data(name)
    get_most_frequent_words(text)
