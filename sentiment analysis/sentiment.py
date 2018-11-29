from data_helpers import *
from tfidf import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import time
start = time.time()
samples, labels = load_data('../data/sentiment/train')
sampels = [clean_doc(doc) for doc in samples]
tv = TfidfVectorizer(max_df=0.6, min_df=20, max_features=3000)
X = tv.fit_transform(samples)
clf = LogisticRegression()
clf.fit(X, labels)

sample_test, label_test = load_data('../data/sentiment/test')
sample_test = [clean_doc(doc) for doc in sample_test]
X_test = tv.transform(sample_test)
y_pred = clf.predict(X_test)
print(classification_report(y_pred, label_test))
end = time.time()
print('Total time:', end - start)