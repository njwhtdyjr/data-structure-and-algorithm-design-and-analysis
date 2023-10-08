
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

def Height(t):			#求二叉树高度的算法
   return _Height(t)

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
def KCount1(t,k):			#解法1：求二叉树第k层结点个数
    cnt=0				#累计第k层结点个数
    qu=deque()                       	#定义一个队列qu
    qu.append(QNode(1,t))		#根结点(层次为1)进队
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




def CompBTree(bt: BTree):  # 在这里输入求解算法
    return _CompBTree(bt.b)
def _CompBTree(t):#判断是不是完全二叉树，采用递归的方法
    #递归出口
    if t == None: return False#这里其实是False还是True都可以，False在某些情况下速度会更快些
    elif t.lchild == None and t.rchild ==None:#如果是一个节点肯定是完全二叉树
        return True
    elif t.rchild !=None and t.lchild == None:#如果只有右孩子，那么一定不是完全二叉树
        return False
    elif t.lchild != None and t.lchild.lchild == None and t.lchild.rchild == None:#如果只有两层而且有左孩子那么一定是完全二叉树
        return True
    #递归
    elif _CompBTree(t.lchild) and _CompBTree(t.rchild):#首先完全二叉树的左右子树也是完全二叉树
        hr = Height(t.rchild)
        hl = Height(t.lchild)#这里只有两种情况才是完全二叉树
        if hl - hr == 1 and KCount1(t.rchild,hr) == 2**(hr-1):#左子树比右子树多一层，而且右子树是满二叉树
            return True
        if hl == hr and KCount1(t.lchild,hl) == 2**(hl-1):#左子树右子树一样多的层数，那么左子树一定是满二叉树
            return True
    return False#其他情况都不是完全二叉树



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

    print(CompBTree(bt))