import sys
import copy
from collections import deque
class SqStack:
    def __init__(self):         #构造方法
      self.data=[]              #存放栈中元素，初始为空
  #栈的基本运算算法
    def empty(self):  # 判断栈是否为空
        if len(self.data) == 0:
            return True
        return False

    def push(self, e):  # 元素e进栈
        self.data.append(e)

    def pop(self):  # 元素出栈
        assert not self.empty()  # 检测栈为空
        return self.data.pop()

    def gettop(self):  # 取栈顶元素
        assert not self.empty()  # 检测栈为空
        return self.data[-1]


class Box:			#方块类
  def __init__(self,i1,j1):  #构造方法
    self.i=i1			#方块的行号
    self.j=j1			#方块的列号
    self.pre=None		#前驱方块


class Box1:			   	#方块类
  def __init__(self,i1,j1,di1):     	#构造方法
    self.i=i1				#方块的行号
    self.j=j1				#方块的列号
    self.di=di1			#di是可走相邻方位的方位号

def mgpath(xi,yi,xe,ye):       #求(xi,yi)到(xe,ye)的一条迷宫路径
  global mg                     	#迷宫数组为全局变量
  global minlen
  dx=[-1,0,1,0]                 	#x方向的偏移量
  dy=[0,1,0,-1]                 	#y方向的偏移量
  qu=deque()                    	#定义一个队列
  b=Box(xi,yi)				#建立入口结点b
  qu.appendleft(b)			#结点b进队
  mg[xi][yi]=-1			#进队方块mg值置为-1
  while len(qu) != 0:  # 队不空时循环
      b = qu.pop()  # 出队一个方块b

      if b.i == xe and b.j == ye:  # 找到了出口,输出路径
          p = b  # 从b出发回推导出迷宫路径并输出
          path = []
          while p != None:  # 找到入口为止
              path.append("[" + str(p.i) + "," + str(p.j) + "]")
              p = p.pre
          minlen = len(path)

          return
      for di in range(4):  # 循环扫描每个相邻方位的方块
          i, j = b.i + dx[di], b.j + dy[di]  # 找b的di方位的相邻方块(i,j)
          if mg[i][j] == 0:  # 找相邻可走方块
              b1 = Box(i, j)  # 建立后继方块结点b1
              b1.pre = b  # 设置其前驱方块为b
              qu.appendleft(b1)  # b1进队
              mg[i][j] = -1  # 进队的方块置为-1
  return False  # 未找到任何路径时返回False

def mgpath_seek(xi,yi,xe,ye):
    global mgback  # 迷宫数组为全局变量
    global minlen
    global minlenpath

    st = SqStack()  # 定义一个顺序栈
    dx = [-1, 0, 1, 0]  # x方向的偏移量
    dy = [0, 1, 0, -1]  # y方向的偏移量
    e = Box1(xi, yi, -1)  # 建立入口方块对象
    st.push(e)  # 入口方块进栈
    mgback[xi][yi] = -1  # 为避免来回找相邻方块,将进栈的方块置为-1
    while not st.empty():  # 栈不空时循环
        b = st.gettop()  # 取栈顶方块,称为当前方块

        if b.i == xe and b.j == ye:  # 找到了出口,输出栈中所有方块构成一条路径
            oneminpath = []
            for k in range(minlen):
                oneminpath.extend([st.data[k].i,st.data[k].j])
            minlenpath.append(oneminpath)

        if len(st.data) >= minlen:
            mgback[b.i][b.j] = 0  # 恢复当前方块的迷宫值
            st.pop()  # 将栈顶方块退栈
            continue    #优化搜索
        find = False  # 否则继续找路径
        di = b.di
        while di < 3 and find == False:  # 找b的一个相邻可走方块
            di += 1  # 找下一个方位的相邻方块
            i, j = b.i + dx[di], b.j + dy[di]  # 找b的di方位的相邻方块(i,j)
            if mgback[i][j] == 0:  # (i,j)方块可走
                find = True
        if find:  # 找到了一个相邻可走方块(i,j)
            b.di = di  # 修改栈顶方块的di为新值
            b1 = Box1(i, j, -1)  # 建立相邻可走方块(i,j)的对象b1
            st.push(b1)  # b1进栈
            mgback[i][j] = -1  # 为避免来回找相邻方块
        else:  # 没有路径可走,则退栈
            mgback[b.i][b.j] = 0  # 恢复当前方块的迷宫值
            st.pop()  # 将栈顶方块退栈
    #在循环内部没有设置return，因为最后st一定会空，所有的路径都会遍历到


    return

if __name__ == '__main__':
    mg=[[1,1,1,1,1,1],  # 载入迷宫数据
     [1,0,1,0,0,1],
     [1,0,0,0,1,1],
     [1,1,0,0,0,1],
     [1,0,0,0,0,1],
     [1,1,1,1,1,1]]
    mgback = copy.deepcopy(mg)#之前的迷宫数据已经修改过，故重新拷贝一份

    [xi,yi] = list(map(int,sys.stdin.readline().split(' '))) # 读入入口位置
    [xe,ye]= list(map(int,sys.stdin.readline().split(' ')))  # 读入出口位置

    minlen = 0
    minlenpath = []
    mgpath(xi, yi, xe, ye)
    mgpath_seek(xi, yi, xe, ye)

    for path in minlenpath:
        print(*path)

