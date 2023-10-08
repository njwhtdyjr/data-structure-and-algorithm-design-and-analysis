import sys

MAXV = 100  # 表示最多顶点个数
INF = 0x3f3f3f3f  # 表示∞


class MatGraph:  # 图邻接矩阵类
    def __init__(self, n=0, e=0):  # 构造方法
        self.n = n  # 顶点数
        self.e = e  # 边数
        self.a = 0
        self.b = 0
        self.edges = [[INF] * MAXV for i in range(MAXV)]  # 邻接矩阵数组
        for i in range(MAXV):  # 主对角线元素置为0
            self.edges[i][i] = 0

    def CreateMatGraph(self):  # 通过文件数据建立图的邻接矩阵
        tmp = sys.stdin.readline().split()  # 读取第1行
        self.a = int(tmp[0])
        self.b = int(tmp[1])
        tmp = sys.stdin.readline().split()  # 读取第2行
        self.n = int(tmp[0])
        self.e = int(tmp[1])
        while True:
            tmp = sys.stdin.readline().split()
            if not tmp: break
            i, j, w = int(tmp[0]), int(tmp[1]), int(tmp[2])
            self.edges[i][j] = w
            self.edges[j][i] = INF

    def DispMatGraph(self):  # 输出图
        for i in range(self.n):
            for j in range(self.n):
                if self.edges[i][j] == INF:
                    print("%4s" % ("∞"), end=' ')
                else:
                    print("%5d" % (self.edges[i][j]), end=' ')
            print()
def Floyd(g):           	    	#输出所有两个顶点之间的最短路径
    A=[[0]*MAXV for i in range(MAXV)]   	#建立A数组
    path=[[0]*MAXV for i in range(MAXV)] 	#建立path数组
    for i in range(g.n):		#给数组A和path置初值即求A-1[i][j]
        for j in range(g.n):
          A[i][j]=g.edges[i][j]
          if i!=j and g.edges[i][j]<INF:
             path[i][j]=i			#i和j顶点之间有边时
          else:
             path[i][j]=-1			#i和j顶点之间没有边时
    for k in range(g.n):			#求Ak[i][j]
        for i in range(g.n):
          for j in range(g.n):
             if A[i][j]>A[i][k]+A[k][j]:
                A[i][j]=A[i][k]+A[k][j]
                path[i][j]=path[k][j]   	#修改最短路径
    Dispath(A,path,g)			#生成最短路径和长度
def Dispath(A,path,g):          	#输出所有的最短路径和长度
       if A[g.a][g.b]!=INF and g.a!=g.b:	#若顶点i和j之间存在路径
          k=path[g.a][g.b]
          apath=[g.b]			#路径上添加终点
          while k!=-1 and k!=g.a:	#路径上添加中间点
             apath.append(k)      	#顶点k加入到路径中
             k=path[g.a][k]
          apath.append(g.a)          	#路径上添加起点
          apath.reverse()           	#逆置apath
          print(*apath)              	#输出最短路径
          print(A[g.a][g.b])

if __name__ == '__main__':
    # 主程序
    g = MatGraph()
    g.CreateMatGraph()
    Floyd(g)