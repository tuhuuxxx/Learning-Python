# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 21:13:19 2018

@author: dang tu
"""
import pickle
def unpickle(file='data/cifar-10-batches-py/data_batch_1'):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict