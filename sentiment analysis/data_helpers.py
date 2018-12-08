import glob
import re

def clean_doc(doc):
    doc = re.sub(r'[.,?,:,\,=,^/,\-,(,),+,;,|,!,*,#,<,>,\',\n]', ' ', doc)
    doc = re.sub(r"\d+.{0,1}\d+", " number ", doc)
    doc = re.sub(r"\d+", " number ", doc)
    doc = re.sub(' +',' ', doc)
    return doc.strip().lower()

def load_data(path='data/sentiment/train'):
    pos_paths = glob.glob(path+'/pos/*.txt')
    neg_paths = glob.glob(path+'/neg/*.txt')
    
    pos_text = []
    for path in pos_paths:
        with open(path, 'r', encoding='utf8') as f:
            text = f.read()
            pos_text.append(text)
    neg_text = []
    for path in neg_paths:
        with open(path, 'r', encoding='utf8') as f:
            text = f.read()
            neg_text.append(text)
    samples = pos_text + neg_text
    labels = [1 for _ in range(len(pos_text))] +  [-1 for _ in range(len(neg_text))]
    return samples, labels