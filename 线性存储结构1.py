# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 16:08:26 2022

@author: kepu
"""
A = [1,3,5]
B = [2,4,6,7]
k = int(input())




def getanswer(k,A,B):
    cnt = 0 #cnt用来记录当前是第几大元素
    m = len(A)
    n = len(B)
    answer = None #answer为第k大的元素
    if k <= (m+n)//2:#根据k较小还是较大进行二分
        while cnt != k:
            if A[m-1] < B[n-1]:
                cnt += 1
                answer = B[n-1]
                n -= 1
            else:
                cnt += 1
                answer = A[m-1]
                m -= 1
        return answer    
    else:
        i = 0
        j = 0
        while cnt != m+n-k+1:#如果k较小，则cnt为倒数第几大元素
            if A[i] < B[j]:
                cnt += 1
                answer = A[i]
                i -= 1
            else:
                cnt += 1
                answer = B[j]
                j -= 1
        return answer
print(getanswer(k,A,B))
                
            
