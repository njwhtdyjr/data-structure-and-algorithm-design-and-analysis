import sys


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
def Height(bt):			#求二叉树高度的算法
   return _Height(bt.b)

def _Height(t):                	#被Height方法调用
  if t==None:
     return 0				#空树的高度为0
  else:
     lh=_Height(t.lchild)	#求左子树高度lchildh
     rh=_Height(t.rchild)	#求右子树高度rchildh
     return max(lh,rh)+1

from collections import deque		#引用双端队列deque
class QNode:				#队列元素类
   def __init__(self,l,p):     	#构造方法
      self.lev=l			#结点的层次
      self.node=p	   		#结点引用
def KCount1(bt,k):			#求二叉树第k层结点列表（填充成满二叉树，空结点以'#'代替），这里节点列表一定是由一层中从左到右的所有结点依次排序而成
    nodes = []				#第k层结点列表
    qu=deque()                       	#定义一个队列qu
    qu.append(QNode(1,bt.b))		#根结点(层次为1)进队
    while len(qu)>0:         		#队不空循环
      p=qu.popleft()			#出队一个结点
      if p.lev>k:			#当前结点的层次大于k，返回nodes
         return nodes
      if p.lev==k:
         nodes.append(p)			#当前结点是第k层的结点,将它加入nodes
      else:				#当前结点的层次小于k
         if p.node.lchild!=None:		#有左孩子时将其进队
             qu.append(QNode(p.lev+1,p.node.lchild))
         else:#没有左孩子时填充以#为数据值的孩子结点，下同
             qu.append(QNode(p.lev+1,BTNode('#')))
         if p.node.rchild!=None:		#有右孩子时将其进队
             qu.append(QNode(p.lev+1,p.node.rchild))
         else:
             qu.append(QNode(p.lev + 1, BTNode('#')))


    return nodes
def Maxsize(bt):#求最大宽度
    h = Height(bt)#先求二叉树高度
    maxsize = 0#最大宽度
    for k in range(1,h+1):#对每一层遍历
        nodes = KCount1(bt,k)
        leng = len(nodes)
        left = 0
        right = leng-1
        for i in range(leng):#先从左遍历nodes，第一个不为#的就是最左的非空结点
            if nodes[i].node.data != '#':
                left = i
                break
        for i in range(leng-1,-1,-1):#再从右遍历
            if nodes[i].node.data !='#':
                right = i
                break
        if right - left +1 >= maxsize:#如果这一层的宽度大于当前的最大宽度，则更新它
            maxsize = right - left +1
    return maxsize
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
    print(Maxsize(bt))