# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 23:13:19 2022

@author: kepu
"""
#获取杨辉三角中第n行（行号从0开始）
def getRow(index):
    #本题思路：定义两个栈，一个队列，addqueue为队列，用于存放临时的两个待加的数
    #tristack为杨辉三角中某行，tempstack为临时存放下一行杨辉三角的栈
    tristack = [1]
    addqueue = []
    #前面的情况较简单，单独列出
    if index == 0:
        return tristack
    tristack = [1,1]
    if index == 1:
        return tristack
    else:
        i = 0
        #i用来控制生成第几行杨辉三角
        while i < index-1:
            j = 0
            
            tempstack = []
            tempstack.append(1)
            
            addqueue.append(tristack.pop())
            addqueue.append(tristack.pop())
            #j用来表示对杨辉三角某一行的元素逐一相加的进行程度
            while j < i+1:
                c = addqueue[0]+addqueue[1]
                
                tempstack.append(c)
                
                addqueue.pop(0)
                if len(tristack) != 0:
                    addqueue.append(tristack.pop())
                j += 1
                
            tempstack.append(1)
            tristack = tempstack
            addqueue = []    
            i += 1
        return tristack
n = int(input())
print(*getRow(n))
 



