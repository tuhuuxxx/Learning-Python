# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 17:49:51 2018

@author: dang tu
"""
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.datasets import fetch_mldata
from sklearn.base import clone

mnist = fetch_mldata('MNIST original')
X, y = mnist['data'], mnist['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

skfolds = StratifiedKFold(n_splits=3, random_state=42)