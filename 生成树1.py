import sys
from collections import deque

MAXV=100							    #表示最多顶点个数
INF=0x3f3f3f3f				            #表示∞

class MatGraph:				            #图邻接矩阵类
    def __init__(self,n=0,e=0):         #构造方法
        self.n=n                        #顶点数
        self.e=e			            #边数
        self.a = 0
        self.b = 0
        self.edges=[[INF]*MAXV for i in range(MAXV)]   #邻接矩阵数组
        for i in range(MAXV):           #主对角线元素置为0
            self.edges[i][i]=0
    def CreateMatGraph(self):  	        #通过文件数据建立图的邻接矩阵
        tmp=sys.stdin.readline().split()        #读取第1行
        self.a =int(tmp[0])
        self.b =int(tmp[1])
        tmp=sys.stdin.readline().split()        #读取第2行
        self.n=int(tmp[0])
        self.e=int(tmp[1])
        while True:
            tmp=sys.stdin.readline().split()
            if not tmp: break
            i,j,w=int(tmp[0]),int(tmp[1]),int(tmp[2])
            self.edges[i][j]=w
            self.edges[j][i]=w
    def DispMatGraph(self):			    #输出图
        for i in range(self.n):
            for j in range(self.n):
                if self.edges[i][j]==INF:
                    print("%4s"%("∞"),end=' ')
                else:
                    print("%5d" %(self.edges[i][j]),end=' ')
            print()
#广度优先遍历寻找边数最少的路径
visited = [0]*MAXV
previsited=['0']*MAXV
def BFS(g,a,b):				#邻接矩阵g中顶点a出发广度优先遍历
  qu=deque()                    	#将双端队列作为普通队列qu
  visited[a]=1				#置已访问标记
  qu.append(a)				#a进队
  while len(qu)>0:              	#队不空循环
    a=qu.popleft()			#出队顶点v
    for w in range(g.n):
      if g.edges[a][w]!=0 and g.edges[a][w]!=INF:
        if visited[w]==0:		#存在边<v,w>并且w未访问
          visited[w]=1	    	#置已访问标记
          previsited[w]=a
          qu.append(w)	  	#w进队
          if w == b:
              break
def sumpath():
    sum = 0
    p = g.b
    q = previsited[p]
    sum += g.edges[p][q]
    while previsited[q] != '0':
        p = q
        q = previsited[p]
        sum += g.edges[p][q]
    return sum

g = MatGraph()
g.CreateMatGraph()
BFS(g,g.a,g.b)
print(sumpath())