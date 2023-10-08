# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 16:07:20 2022

@author: kepu
"""

#定义双链表类和链表节点类
class DLinknode:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prior = None
class DLinktab:
    def __init__(self):
        self.head = DLinknode()
        self.tail = self.head
        self.size = 0
    def add(self,node):
        if self.head.next == None:
            self.head.next = node
            self.head.next.prior = self.head
            self.tail = self.head.next
        else:
            self.tail.next = node
            self.tail.next.prior = self.tail
            self.tail = self.tail.next
        self.size += 1
    #此处采用从两边夹逼的办法，逐个判断值是否相等，flag是是否是回文的标志
    def isPalindrome(self):
        p = self.head.next
        q = self.tail
        flag = True
        while q.next != p and p != q:#如果链表大小是偶数，则用q.next != q,如果是奇数则用p != q
            if p.data == q.data:
                p = p.next
                q = q.prior
            else:
                flag = False
                break
        return flag
linkdata = list(map(int,input().split()))
linknodes = []
for data in linkdata:
    linknodes.append(DLinknode(data))

link = DLinktab()
for node in linknodes:
    link.add(node)
print(link.isPalindrome())