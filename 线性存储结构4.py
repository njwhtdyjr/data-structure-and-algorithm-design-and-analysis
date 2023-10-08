# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 11:47:00 2022

@author: kepu
"""
#定义单链表类和链表节点类
class Linknode:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class Linktab:
    def __init__(self):
        self.head = Linknode()
        self.tail = self.head
    def add(self,node):
        if self.head.next == None:
            self.head.next = node
            self.tail = self.head.next
        else:
            self.tail.next = node
            self.tail = self.tail.next

#初始化单链表
A = Linktab()
B1 = Linktab()
B2 = Linktab()
for i in range(1,6):
    A.add(Linknode(i))
for i in range(2,5):
    B1.add(Linknode(i))
B2.add(Linknode(1))
B2.add(Linknode(3))
B2.add(Linknode(4))

#定义判断连续子序列的方法    
def subsequence(A,B):
    p = A.head
    q = B.head
    flag = 0#flag用来标识是否已经有相同元素
    while q.next != None:
        if p.next.data == q.next.data:
            p = p.next
            q = q.next
            flag = 1
        else:
            p = p.next
            if flag:#如果有相同元素却不连续则跳出循环，并标记flag = 0
                flag = 0
                break
    return flag #flag用来表示是否连续
answer1 = subsequence(A,B1)
answer2 = subsequence(A,B2)

def getanswer(answer):
    if answer:
        print('是')
    else:
        print('否')
getanswer(answer1)
getanswer(answer2)