
import pandas as pd
from nltk import word_tokenize
from nltk.corpus import stopwords
import string
from nltk.stem.snowball import SnowballStemmer

class CleanData:

    def dataset_tokanization(self,text):
        text = word_tokenize(text)
        return " ".join(text)

    def  stop_words(self, text):
         sw = set(stopwords.words('english'))
         new_stopwords = [',', '.', 'THE', '?', 'The', ')', '(', '‘', '’', 'an', '*', '½', 'ï', '<', '>', '\w', '\d','�',
                          '\s']
         sw = sw.union(new_stopwords)
         text = [word.lower() for word in text.split() if word.lower() not in sw]
         return " ".join(text)



    def remove_punctuation(self,text):
        # replacing the punctuations with no space,         # which in effect deletes the punctuation marks
        translator = str.maketrans('', '',string.punctuation)  # return the text stripped of punctuation marks
        return text.translate(translator)


    def perform_stemming(self, text):
        stemmer = SnowballStemmer("english")
        text = [stemmer.stem(word) for word in text.split()]
        return " ".join(text)


    def cleaning(self):
        data = pd.read_csv(r"C:\Users\Sanau\PycharmProjects\Assignment_04_DM\App\preprocessing\spam.csv",names=['v1','v2'],encoding='latin-1')  # removing stop words from Content column and Title column
        data['content'] = data['v2'].fillna("")
        data['content'] = data['content'].apply(self.dataset_tokanization)
        data['content'] = data['content'].apply(self.stop_words)
        data['content'] = data['content'].apply(self.remove_punctuation)
        #data['content'] = data['content'].apply(self.perform_stemming)
        data['content'] = data['content'].str.lower()
        dataset = data.drop('v2', axis=1)
        print(dataset)
        dataset.to_csv(r"C:\Users\Sanau\PycharmProjects\Assignment_04_DM\App\classification\dataset.txt", sep=',', index=False)

#cd = CleanData()

#cd.cleaning()