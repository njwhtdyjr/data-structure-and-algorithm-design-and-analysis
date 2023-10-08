# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 21:36:27 2022

@author: kepu
"""

L = [1,2,1,2,3,1]

#nodepulicate 用来去重
def nodepulicate(L):
    j = 0
    while j < len(L):
        k = L[j]
        i = j+1
       
        while i < len(L):#去除重复元素
            
            if L[i] == k:
                L.pop(i)
            else: 
                i += 1
        j += 1
    return len(L)
       

print(nodepulicate(L))
