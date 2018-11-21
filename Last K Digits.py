# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 09:53:35 2018

@author: dang tu
"""
import time

def find_k_digits(x, y, p):
    res = 1
    x = x%p
    
    while y > 0:
        if y & 1:
            res = (res*x)%p
        y = y >> 1
        x = (x*x)%p
    return res

if __name__ == "__main__":
    gt = 0
    start = time.time()
    for i in range(1, 10**7):
        gt += find_k_digits(i, i, 10**9)
    end = time.time()
    print(gt%(10**9))
    print(end-start)