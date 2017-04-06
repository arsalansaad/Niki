# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:55:05 2017

@author: HP
"""

alph = list(map(chr, range(65, 91)))

alph = [None] + alph

m = int(raw_input())
n = int(raw_input())

for i in range(m,n+1):
    if i <= 26:
        print alph[i]
    else:
        print alph[int(i/26)]+alph[i%26]