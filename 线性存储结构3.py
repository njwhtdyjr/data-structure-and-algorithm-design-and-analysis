# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 22:23:29 2022

@author: kepu
"""

L = list(map(int,input().split()))
def removeDuplicates(L):
    i = 0
    j = 1
    
    while j < len(L):
       if L[j] == L[i] and j == i+1:
           j += 1
       elif L[j] == L[i]:
           L.pop(j)
       else:
           i = j
           j += 1
           
    return len(L)
print(removeDuplicates(L))
print(*L)       