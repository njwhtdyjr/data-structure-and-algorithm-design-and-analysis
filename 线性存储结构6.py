# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 15:03:15 2022

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
        
    #此题根据k的大小进行判断，如果k刚好整除self.size（也就是链表大小），那么不需移动
    #注意到只需要更改几个有关节点的指针域
    #如果k比较小，那么从尾部前溯会快一点，k比较大，从首部后推会快点
    def getnode(self,k): #这个是为了找到旋转后成为首节点的节点
        k2 = k%self.size
        cnt = 1
        p = self.head
        q = self.tail
        if k2 <= self.size//2 + 1:
            while cnt < k2:
                q = q.prior
                cnt += 1
            return q
        else:
            while cnt-2 < self.size - k2:
                p = p.next
                cnt += 1
            return p
    def totateRight(self,k):#这个是真正的旋转链表函数
        if k%self.size == 0:
            return
        else:#更改指针域，具体过程可以画图理解，这里不多解释
            p = self.getnode(k)
            q = self.tail
            r = self.head
            r.next.prior = q
            q.next = r.next
            r.next = p
            p.prior.next = None
            p.prior = r
            
            return 
    def display(self):#展示旋转后的链表
        nodelist = []
        p =self.head
        while p.next != None:
            p = p.next
            nodelist.append(p.data)
        return nodelist
#输入并生成链表  
linkdata = list(map(int,input().split()))
linknodes = []
for data in linkdata:
    linknodes.append(DLinknode(data))

link = DLinktab()
for node in linknodes:
    link.add(node)

k = int(input())

link.totateRight(k)
print(*link.display())