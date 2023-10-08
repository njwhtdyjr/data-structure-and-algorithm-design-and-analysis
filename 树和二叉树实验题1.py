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

def Preorder(t):#遍历以t为根节点的二叉树，判断是否含有child1或child2中的一个
    global child1, child2#child1 child2 即为我们需要找最近公共祖先的两个节点
    if t == None:return False
    if t.data == child1 or t.data == child2:
        return True
    if Preorder(t.lchild) or Preorder(t.rchild):
        return True
    return False

def closeancestor(bt):
    global child1, child2
    global data
    if child1 not in data[0] or child2 not in data[0]:#如果有child不在结点列表中，说明没有公共祖先
        return None
    elif bt.b.data == child1 or bt.b.data == child2:#如果根节点就是child1或child2，那么根节点就是最近公共祖先
        return bt.b.data
    else:#分三种情况，一：如果左右子树都有child，说明本身是最近公共祖先
        if Preorder(bt.b.lchild) and Preorder(bt.b.rchild):
            return bt.b.data
        elif Preorder(bt.b.lchild):#二：只有左子树有child，则将结点转移至左孩子
            return _closeancestor(bt.b.lchild)
        else:#三：只有右子树有child，则将结点转移至右孩子
            return _closeancestor(bt.b.rchild)

def _closeancestor(t):
    global child1, child2#如果结点自身就是child则自身就是最近公共祖先
    if t.data == child1 or t.data == child2:
        return t.data
    elif Preorder(t.lchild) and Preorder(t.rchild):#道理同上，递归定义
        return t.data
    elif Preorder(t.lchild):
        return _closeancestor(t.lchild)
    else:
        return _closeancestor(t.rchild)

if __name__ == '__main__':
    data = []
    data.append(list(sys.stdin.readline().split(' ')))
    for i in range(1, 5):
        str = sys.stdin.readline()
        if str.find('null'):
            data.append(list(map(int, str.split(' '))))
        else:
            data.append([])
    child1, child2 = list(input().split())#child1 child2 为两个节点
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
    print(closeancestor(bt))