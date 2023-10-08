import sys

MAXV=100							    #表示最多顶点个数
INF=0x3f3f3f3f				            #表示∞

class MatGraph:				            #图邻接矩阵类
    def __init__(self,n=0,e=0):         #构造方法
        self.n=n                        #顶点数
        self.e=e			            #边数
        self.edges=[[INF]*MAXV for i in range(MAXV)]   #邻接矩阵数组
        for i in range(MAXV):           #主对角线元素置为0
            self.edges[i][i]=0
    def CreateMatGraph(self):  	        #通过文件数据建立图的邻接矩阵
        tmp=sys.stdin.readline().split()        #读取第1行
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
def Prim(g,v):                  	#求最小生成树
    lowcost=[0]*MAXV	        	#建立数组lowcost
    closest=[0]*MAXV			#建立数组closest
    weight = 0
    for i in range(g.n):		#给lowcost[]和closest[]置初值
        lowcost[i]=g.edges[v][i]
        closest[i]=v
    for i in range(1,g.n):   		#找出最小生成树的n-1条边
      min=INF
      k=-1
      for j in range(g.n):		#在(V-U)中找出离U最近的顶点k
        if lowcost[j]!=0 and lowcost[j]<min:
           min=lowcost[j]
           k=j	        		#k记录最小顶点的编号
      weight += min
      lowcost[k]=0		   		#将顶点k加入U中
      for j in range(g.n):		#修改数组lowcost和closest
        if lowcost[j]!=0 and g.edges[k][j]<lowcost[j]:
           lowcost[j]=g.edges[k][j]
           closest[j]=k
    return weight

g = MatGraph()
g.CreateMatGraph()
print(Prim(g,0))

