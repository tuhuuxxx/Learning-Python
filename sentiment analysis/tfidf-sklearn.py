from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from data_helpers import *
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier, VotingClassifier, BaggingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
import time

import numpy as np
from SGD import SGD

if __name__ == "__main__":
    start = time.time()
    samples, labels = load_data('../data/small sentiment/train')
    samples = [clean_doc(doc) for doc in samples]
    tv = TfidfVectorizer(min_df = 5, max_df = 0.5, max_features=5000)
#    tv = CountVectorizer()  
    X = tv.fit_transform(samples)
    
    sample_test, label_test = load_data('../data/small sentiment/test')
    sample_test = [clean_doc(doc) for doc in sample_test]
    X_test = tv.transform(sample_test)
    '''
    log_clf = LogisticRegression(C=1.5)
    mlp_clf = MLPClassifier(hidden_layer_sizes=(100,100,100,))
    rf_clf = RandomForestClassifier(max_depth=30)
    mb_clf = MultinomialNB()
    svm_clf = LinearSVC(C=0.1)
    sgd_clf = SGDClassifier(loss="hinge", penalty="l2")
    
    estimators=[('lr', log_clf),
                ('mlp', mlp_clf), 
                ('rf', rf_clf),
                ('mb', mb_clf),
                ('svm', svm_clf),
                ('sgd', sgd_clf)]
    
    voting_clf = VotingClassifier(
            estimators=estimators,
            voting='hard')
    
    for clf in (log_clf,mlp_clf,rf_clf,mb_clf,svm_clf,sgd_clf,voting_clf):
        clf.fit(X, labels)
        y_pred = clf.predict(X_test)
        print(clf.__class__.__name__, accuracy_score(label_test, y_pred))
        
    clf = BaggingClassifier(
            LogisticRegression(),
            n_estimators=100,
            max_samples=2000, 
            bootstrap=True,
            n_jobs=-1,
            oob_score=True)
    '''
    X = X.toarray()
    X_test = X_test.toarray()
    Y = np.array(labels)
    sgd = SGD()
    sgd.fit(X, Y)
    y_pred = sgd.predict(X_test)
    print(accuracy_score(label_test, y_pred))
    end = time.time()
    print(end  - start)