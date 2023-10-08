# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:41:30 2022

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
#输入数据并生成相应单链表
linkdata = list(map(int,input().split()))
linknodes = []
for data in linkdata:
    linknodes.append(Linknode(data))

link = Linktab()
for node in linknodes:
    link.add(node)
#去重函数同时存储不重复的元素
def moveDuplicate_and_display(link):
    p = link.head
    lis = []#lis用来存储不重复元素
    while p.next != None:
        if p.next.data == p.data:
            p.next = p.next.next#因为链表排序，所以可以直接通过相邻元素是否重复来去重
        else:
            p = p.next
            lis.append(p.data)
    return lis
print(*moveDuplicate_and_display(link))       
            