# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 12:36:09 2017

@author: HP
"""

from math import sqrt

def is_prime(n):
    if n == 1:
        return 'Prime'
    f = 0
    for i in range(1,int(n/2)+1):
        if n%i == 0:
            f+=1
    if f == 1:
        return 'Prime'
    return 'Not Prime'

def factors(n):    
    results = set()
    for i in range(1,int(sqrt(n))+1):
        if n % i == 0:
            results.add(i)
            results.add(int(n/i))
    return sorted(list(results))[1:]

a = int(raw_input())

for item in factors(a):
    print item,is_prime(item)