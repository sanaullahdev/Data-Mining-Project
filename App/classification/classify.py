import pandas as pd
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
sws = set(stopwords.words('english'))
new_stopwords = [',', '.', 'the', '?', 'The','I','u','U','T','C','0','1','2','3','4','5','6','7','8','9','10', ')', '(', '‘', '’', 'an', '*', '½', 'ï', '<', '>', '\w', '\d', '�','\s']
sw = sws.union(new_stopwords)
new_stopwords_list = stop_words.union(new_stopwords)
import io,re
from nltk import word_tokenize
class classify:

    dataset=pd.read_csv(r'C:\Users\Sanau\PycharmProjects\Assignment_04_DM\App\preprocessing\dataset.txt',names=['category','content']
                        )
    number = 0
    ham = []
    spam=[]
    for i in dataset.category:
        if i=="ham":
            ham.append(dataset.content[number])
            # print(dataset.content[number])
        number += 1
    number=0
    for i in dataset.category:
        if i=="spam":
            spam.append(dataset.content[number])
            #print(dataset.content[number])
        number += 1
    print(ham)
    print("next%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print(spam)
    with io.open("spam.txt", "w", encoding="utf-8") as filehandle:
        for listitems in spam:
            filehandle.write('%s\n' % listitems)
    with io.open("ham.txt", "w", encoding="utf-8") as filehandle:
        for listitems in ham:
            filehandle.write('%s\n' % listitems)


    def model(category,filename):
        wlist = []
        filters = []
        for data in category:
            token = word_tokenize(data)
            text = [word.lower() for word in token if word.lower() not in new_stopwords_list]
            for w in text:
                filters.append(w)
        print(filters)
        from collections import Counter
        wlist.append(Counter(filters).most_common(2000))
        print(wlist)
        str1 = ' '.join([str(elem) for elem in wlist])
        string2 = str1.replace('(', '')
        string2 = string2.replace('[', '')
        string2 = string2.replace(')]', '')
        defs = string2.split("), ")
        defs = [x.lower() for x in defs]
        print(defs)


        #print(defs)
        with io.open(filename, "w", encoding="utf-8") as filehandle:
            filehandle.write(("words,quantity\n"))
            for listitems in defs:
                filehandle.write('%s\n' % listitems)
    model(ham,"ham_words.txt")
    model(spam,"spam_words.txt")


    #assigning one two
    dataset1 = pd.read_csv('ham_words.txt',names=['words','category'])
    dataset2 = pd.read_csv('spam_words.txt',names=['words','category'])
    #print(dataset1)
    number = 0
    train_data = []

    for i in dataset1.words:
#        print(i)
        train_data.append(i+",one")


 #   print(train_data)
    for i in dataset2.words:
        train_data.append(i+",two")
    #print(train_data)
    with io.open("trainset.txt", "w", encoding="utf-8") as filehandle:
        for listitems in train_data:
            filehandle.write('%s\n' % listitems)

    #category
    def category(self,data):
        data1 = pd.read_csv('trainset.txt',
                   names=['words','category'])
        article=[]
        num=0
        ham=0
        spam=0
        train=[]
        token = word_tokenize(data)
        filters = [word for word in token if word not in new_stopwords_list]
        filters = []
        for w in token:
            if w not in new_stopwords_list:
                filters.append(w)
                filters=list(dict.fromkeys(filters))
                filters=[x.lower() for x in filters]

        for i in data1.category:
            if i=="one":
                abc=data1.words[num]
                train.append(abc.replace("'",''))
                #print(train)
                for k in filters:
                    #print(train[num],k)
                    if(train[num]==k):
                        print(train[num], k)
                        ham+=1
                num+=1
        print(ham)
        print("one complete")
        for i in data1.category:
            if i=="two":
                abc = data1.words[num]
                train.append(abc.replace("'", ''))
                for k in filters:
                    #print(train[num],k)
                    if(train[num]==k):
                        #print(train[num],k)
                        #print(k)
                        spam+=1
                num+=1
        print("two complete")
        print(ham,spam)
        if ham>spam:
            print("category is ham")
            return "ham"
        if spam>ham:
            print("category is spam")
            return "spam"
        if spam==ham:
            print("Text is too small to predict category")
            return "Text is too small to predict category"
    text="per request melle melle oru minnaminunginte nurungu vettam  set callertune callers press 9 copy friends callertune"
#    category(text)