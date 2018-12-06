from collections import Counter
import math
import numpy as np
from scipy.sparse import csr_matrix

class TfidfVectorizer():
    def __init__(self, max_df=1.0, min_df=1, max_features=None):
        self.max_df = max_df
        self.min_df = min_df
        self.max_features = max_features
        self.vocab = None
        self.idf_dict = {}
        
    def fit_transform(self, corpus):
        all_text_list = ' '.join(corpus).split()
        if self.max_features is None:
            self.vocab = list(set(all_text_list))
        else:
            # remain the top max_features ordered by term frequency across the corpus
            word_dict = Counter(all_text_list)
            self.vocab = [item[0] for item in word_dict.most_common(self.max_features)]
        self.vocab_size = len(self.vocab)
        
        self.idf_dict = self.idf(corpus)
        X = []
        for doc in corpus:
            X.append([self.tf(word, doc)*self.idf_dict[word] for word in self.vocab])
        X = csr_matrix(X)
        return X
    ''' 
    def transform(self, corpus):
        X = []
        for doc in corpus:
            X.append([self.tf(word, doc)*self.idf_dict[word] for word in self.vocab])
        X = csr_matrix(X)
        return X
    '''
    def transform(self, corpus):
        X = []
        for doc in corpus:
            words = set(doc.split())
            temp = [0 for _ in range(self.vocab_size)]
            for word in words:
                if word in self.vocab:
                    temp[self.vocab.index(word)] = self.tf(word, doc)*self.idf_dict[word]
            X.append(temp)
        X = csr_matrix(X)
        return X
      
    def get_feature_names(self):
        return self.vocab
    
    def tf(self, word, doc):
        return doc.split().count(word)/len(doc.split())
    
    def idf(self, corpus):
        idf_dict = {}
        n_corpus = len(corpus)
        corpus = [set(doc.split()) for doc in corpus]
        for word in self.vocab:
            n = sum([1 for doc in corpus if word in doc])
            idf_dict.update({word: math.log10(n_corpus/n)})
        return idf_dict

if __name__ == "__main__":
    doc1 = 'this is a a sample'
    doc2 = 'this is another another example example example'
    doc3 = 'i love a girl'
    corpus = [doc1, doc2, doc3]
    
    doc4 = 'i like her'
    doc5 = 'i love her so much'
    corpus2 = [doc4, doc5]
    tv = TfidfVectorizer()
    X = tv.fit_transform(corpus)
    Y = tv.transform(corpus2)
    print(Y)
    
    
        

    
    