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


def RePreOrder(bt: BTree):  # 在这里输入求解算法
    _RePreOrder(bt.b)
def _RePreOrder(t):
    global res
    if t == None:return
    _RePreOrder(t.rchild)#按照RNL的次序遍历二叉树，如果是叶子结点则将它加入res
    if t.rchild == None and t.lchild == None:
        res.append(t.data)
    _RePreOrder(t.lchild)
    return
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
    res = []
    RePreOrder(bt)
    print(*res)