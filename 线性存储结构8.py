# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:04:07 2022

@author: kepu
"""
#定义多项式类
class Poly:
    def __init__(self,nums):
        #list_index存放指数，list_covar存放系数
        self.list_index = []
        self.list_covar = []
        #添加系数和指数
        num = len(nums)
        for i in range(0,num,2):
           self.list_covar.append(nums[i])
           self.list_index.append(nums[i+1])

p1 = Poly(list(map(int,input().split()))) 
p2 = Poly(list(map(int,input().split()))) 
#定义多项式的加法，该方法采用打印的方式输出要输出的值，减少了存储输出值的空间
def polyadd(p1,p2):
    i = 0
    j = 0
    p = p1.list_index
    q = p2.list_index
    r = p1.list_covar
    s = p2.list_covar
    
    #从左往右逐一比较系数大小
    while i < len(p) and j < len(q) :
        if p[i] > q[j]:
            
            print(r[i],p[i],end=' ')
            i += 1
        
        elif p[i] < q[j]:
            print(s[j],q[j],end=' ')
            j += 1
        
        else:
            print(r[i]+s[j],p[i],end=' ')
            i += 1
            j += 1
    #如果其中有一个多项式已遍历完，则进行如下处理
    while i < len(p)-1:
        print(r[i],p[i],end=' ')
        i += 1
    while j < len(q)-1:
        print(s[j],q[j],end=' ')
        j += 1
    #如果是最后一项，注意到结尾没有空格，故单独考虑该情况
    if i == len(p)-1:
        print(r[i],p[i])
    if j == len(q)-1:
        print(s[j],q[j])
    
  
polyadd(p1,p2)





