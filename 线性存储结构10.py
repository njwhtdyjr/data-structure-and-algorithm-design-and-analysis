# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 21:39:43 2022

@author: kepu
"""
#用三个列表存放三个整数集合
a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))
a3 = list(map(int,input().split()))
#本题思路：定义三个指针，都从整数集合中最小的数开始，每次都上移三元组中最小的数，这样最多遍历（m+n+k）次
#途中记录下出现过的最小值和最小值对应的三元组
#同时为了求出所有的最小三元组，有一些细节需要考虑
#本题中有许多模块高度复用，但是由于变量作用域的问题，没有用函数实现
#mindis 最小距离 #minarr 最小三元组
mindis = abs(a1[0]-a2[0])+abs(a3[0]-a2[0])+abs(a1[0]-a3[0])
minarr = [[a1[0],a2[0],a3[0]]]
#定义在三个数中获取最小数的方法
def getmin3(i1,i2,i3):
    if a1[i1]>=a2[i2]:
        if a2[i2]>=a3[i3]:
            return 3
        else:
            return 2
    elif a1[i1]>=a3[i3]:
        return 3
    else:
        return 1


i1 = 0
i2 = 0
i3 = 0
while i1 < len(a1) and i2 < len(a2) and i3 < len(a3):
    #temmindis用来存放暂时的距离，比较并存储最小值
    temmindis = abs(a1[i1]-a2[i2])+abs(a3[i3]-a2[i2])+abs(a1[i1]-a3[i3])
    if temmindis < mindis:
        mindis = temmindis
        minarr = [[a1[i1],a2[i2],a3[i3]]]
    elif temmindis == mindis:
        minarr.append([a1[i1],a2[i2],a3[i3]])
    #获取最小值并上移指针
    i = getmin3(i1,i2,i3)
    
    if i == 1:
        #该特殊情况为三元组中可能同时出现两个最小值
        if a1[i1] == a2[i2] and i2+1 < len(a2):
            i2 += 1
            temmindis = abs(a1[i1]-a2[i2])+abs(a3[i3]-a2[i2])+abs(a1[i1]-a3[i3])
            if temmindis < mindis:
                mindis = temmindis
                minarr = [[a1[i1],a2[i2],a3[i3]]]
            elif temmindis == mindis:
                minarr.append([a1[i1],a2[i2],a3[i3]])
            i2 -= 1
        if a1[i1] == a3[i3] and i3+1 < len(a3):
             i3 += 1
             temmindis = abs(a1[i1]-a2[i2])+abs(a3[i3]-a2[i2])+abs(a1[i1]-a3[i3])
             if temmindis < mindis:
                 mindis = temmindis
                 minarr = [[a1[i1],a2[i2],a3[i3]]]
             elif temmindis == mindis:
                 minarr.append([a1[i1],a2[i2],a3[i3]])
             i3 -= 1  
        i1 += 1
        
        
                 
    elif i == 2:
        if a1[i1] == a2[i2] and i1+1 < len(a1):
            i1 += 1
            temmindis = abs(a1[i1]-a2[i2])+abs(a3[i3]-a2[i2])+abs(a1[i1]-a3[i3])
            if temmindis < mindis:
                mindis = temmindis
                minarr = [[a1[i1],a2[i2],a3[i3]]]
            elif temmindis == mindis:
                minarr.append([a1[i1],a2[i2],a3[i3]])
            i1 -= 1
        if a2[i2] == a3[i3] and i3+1 < len(a3):
             i3 += 1
             temmindis = abs(a1[i1]-a2[i2])+abs(a3[i3]-a2[i2])+abs(a1[i1]-a3[i3])
             if temmindis < mindis:
                 mindis = temmindis
                 minarr = [[a1[i1],a2[i2],a3[i3]]]
             elif temmindis == mindis:
                 minarr.append([a1[i1],a2[i2],a3[i3]])
             i3 -= 1  
        i2 += 1
       
    else:
        if a1[i1] == a3[i3] and i1+1 < len(a1):
            i1 += 1
            temmindis = abs(a1[i1]-a2[i2])+abs(a3[i3]-a2[i2])+abs(a1[i1]-a3[i3])
            if temmindis < mindis:
                mindis = temmindis
                minarr = [[a1[i1],a2[i2],a3[i3]]]
            elif temmindis == mindis:
                minarr.append([a1[i1],a2[i2],a3[i3]])
            i1 -= 1
        if a2[i2] == a3[i3] and i2+1 < len(a2):
             i2 += 1
             temmindis = abs(a1[i1]-a2[i2])+abs(a3[i3]-a2[i2])+abs(a1[i1]-a3[i3])
             if temmindis < mindis:
                 mindis = temmindis
                 minarr = [[a1[i1],a2[i2],a3[i3]]]
             elif temmindis == mindis:
                 minarr.append([a1[i1],a2[i2],a3[i3]])
             i2 -= 1  
        i3 += 1
#可能出现有一个整数集合已经遍历完          
if i1 == len(a1):
    i1 -= 1
    #现在只需要比较其他两个整数集合的最小值
    while True:
        if a2[i2]>=a3[i3]:
            i3 += 1
            if i3 == len(a3):
                break
        else:
            i2 += 1
            if i2 == len(a2):
                break
        #仍然是记录最小值
        temmindis = abs(a1[i1]-a2[i2])+abs(a3[i3]-a2[i2])+abs(a1[i1]-a3[i3])
        if temmindis < mindis:
            mindis = temmindis
            minarr = [[a1[i1],a2[i2],a3[i3]]]
        elif temmindis == mindis:
            minarr.append([a1[i1],a2[i2],a3[i3]])
        #如果出现上移指针，三元组距离大于原来的最小值，则不用继续遍历下去
        else:
            break
elif i2 == len(a2):
    i2 -= 1
    while True:
        if a1[i1]>=a3[i3]:
            i3 += 1
            if i3 == len(a3):
                break
        else:
            i1 += 1
            if i1 == len(a1):
                break
        temmindis = abs(a1[i1]-a2[i2])+abs(a3[i3]-a2[i2])+abs(a1[i1]-a3[i3])
        if temmindis < mindis:
            mindis = temmindis
            minarr = [[a1[i1],a2[i2],a3[i3]]]
        elif temmindis == mindis:
            minarr.append([a1[i1],a2[i2],a3[i3]])
        else:
            break
elif i3 == len(a3):
    i3 -= 1
    while True:
        if a2[i2]>=a1[i1]:
            i1 += 1
            if i1 == len(a1):
                break
        else:
            i2 += 1
            if i2 == len(a2):
                break
        temmindis = abs(a1[i1]-a2[i2])+abs(a3[i3]-a2[i2])+abs(a1[i1]-a3[i3])
        if temmindis < mindis:
            mindis = temmindis
            minarr = [[a1[i1],a2[i2],a3[i3]]]
        elif temmindis == mindis:
            minarr.append([a1[i1],a2[i2],a3[i3]])
        else:
            break
        
print(mindis)
for arr in minarr:
    
    print(*arr)  
