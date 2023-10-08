import sys
from collections import deque

class QNode:				#队列元素类
   def __init__(self,l,p):     	#构造方法
      self.lev=l			#结点的层次
      self.node=p	   		#结点引用
def KCount1(bt,k):			#解法1：求二叉树第k层结点个数
   cnt=0				#累计第k层结点个数
   qu=deque()                       	#定义一个队列qu
   qu.append(QNode(1,bt.b))		#根结点(层次为1)进队
   while len(qu)>0:         		#队不空循环
      p=qu.popleft()			#出队一个结点
      if p.lev>k:			#当前结点的层次大于k，返回cnt
         return cnt
      if p.lev==k:
         cnt+=1			#当前结点是第k层的结点,cnt增1
      else:				#当前结点的层次小于k
         if p.node.lchild!=None:		#有左孩子时将其进队
            qu.append(QNode(p.lev+1,p.node.lchild))
         if p.node.rchild!=None:		#有右孩子时将其进队
            qu.append(QNode(p.lev+1,p.node.rchild))
   return cnt
class BTNode:  # 二叉链中结点类
    def __init__(self, d=None):  # 构造方法
        self.data = d  # 结点值
        self.lchild = None  # 左孩子指针
        self.rchild = None  # 右孩子指针


class BTree:  # 二叉树类
    def __init__(self, d=None):  # 构造方法
        self.b = None  # 根结点指针

    def SetRoot(self, r):  # 设置根结点为r
        self.b = r


def Width(bt: BTree):  # 在这里输入求解算法
    width = []
    for k in range(1,len(data[0])+1):#层次数最多为len(data[0])，因为最多层是每层只有一个节点，而对于没有节点的层次，cnt=0
        width.append(KCount1(bt,k))#求出每一层的结点个数
    return max(width)

# 主程序
if __name__ == '__main__':
    data = []
    data.append(list(sys.stdin.readline().split(' ')))
    for i in range(1, 5):
        str = sys.stdin.readline()
        if str.find('null'):
            data.append(list(map(int, str.split(' '))))
        else:
            data.append([])
    nl = []
    for i in range(len(data[0])):
        nl.append(BTNode(data[0][i]))
    if len(data[1]) > 0:
        for i in range(len(data[1])):
            nl[data[1][i]].lchild = nl[data[2][i]]
    if len(data[3]) > 0:
        for i in range(len(data[3])):
            nl[data[3][i]].rchild = nl[data[4][i]]
    bt = BTree()
    bt.SetRoot(nl[0])
    print(Width(bt))