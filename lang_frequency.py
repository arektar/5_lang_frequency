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
    inv = dict()
    for key in frequancy:
        val = frequancy[key]
        if val not in inv:
            inv[val] = [key]
        else:
            inv[val].append(key)
    keys=list(inv.keys())
    keys.sort()
    keys.reverse()
    i=10
    for key in keys:
        try:
            for one in inv[key]:
                print(str(key) + " : " + one),
                i=i-1
                if i==0:raise
        except:
            if i!=0:
                print("текст закончился")
            break


if __name__ == '__main__':
    name=input("Write full file name: ")
    text=load_data(name)
    get_most_frequent_words(text)
