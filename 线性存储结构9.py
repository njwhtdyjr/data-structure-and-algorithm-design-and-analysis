# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:40:01 2022

@author: kepu
"""
#定义多项式类如第一题
class Poly:
    def __init__(self,nums):
        self.list_index = []
        self.list_covar = []
        num = len(nums)
        for i in range(0,num,2):
           self.list_covar.append(nums[i])
           self.list_index.append(nums[i+1])
           
p = Poly(list(map(int,input().split()))) 
x = int(input())
#定义求值函数，采用秦九韶算法
def getvalue(p,x):
    
    j = 0
    result = p.list_covar[0]
    
    k = len(p.list_covar)
    #如果该多项式只有一项，则直接执行计算
    if k == 1:
        return result*x**p.list_index[0]
    #注意到多项式中可能出现有些指数的系数为0
    while  j < k-1 :
        j += 1
        result = result*x**(p.list_index[j-1]-p.list_index[j])+p.list_covar[j]
    #如果while 循环后最后的指数不是0的话，那么还需要进行如下处理
    if  p.list_index[j] != 0:
        result = result*x**p.list_index[j]
    return result
result = getvalue(p,x)
print(result)



