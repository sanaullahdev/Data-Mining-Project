from nltk.corpus import stopwords

sw = set(stopwords.words('english'))
new_stopwords = [',', '.', 'THE', '?', 'The', ')', '(', '‘', '’', 'an', '*', '½', 'ï', '<', '>', '\w', '\d','�',
                          '\s']
sw = sw.union(new_stopwords)


string ="Romila is a girl who illu illu the Muzammil"
for word in string:
    print(word)
    if word.lower() not in sw:
        text=word.lower()