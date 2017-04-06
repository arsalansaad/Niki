# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:43:33 2017

@author: HP
"""

n = int(raw_input("Enter the length of list: "))
lst = []
for i in range(n):
    lst.append(raw_input())
    
print sorted(lst,key=len)