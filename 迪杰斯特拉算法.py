import sys
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
def Dijkstra1(g,v):         	      	#求从v到其他顶点的最短路径
    dist=[-1]*MAXV			#建立dist数组
    path=[-1]*MAXV			#建立path数组
    S=[0]*MAXV				#建立S数组
    for i in range(g.n):
      dist[i]=g.edges[v][i]		#最短路径长度初始化
      if g.edges[v][i]<INF:		#最短路径初始化
        path[i]=v			#v到i有边置路径上顶点i的前驱为v
      else:				#v到i没边置路径上顶点i的前驱为-1
        path[i]=-1
    S[v]=1				#源点v放入S中
    u=-1
    for i in range(g.n-1):		#循环向S中添加n-1个顶点
       mindis=INF				#mindis置最小长度初值
       for j in range(g.n):		#选取不在S中且具有最小距离的顶点u
          if S[j]==0 and dist[j]<mindis:
             u=j
             mindis=dist[j]
       S[u]=1				#顶点u加入S中
       for j in range(g.n):		#修改不在s中的顶点的距离
         if S[j]==0:			#仅仅修改S中的顶点j
            if g.edges[u][j]<INF and dist[u]+g.edges[u][j]<dist[j]:
               dist[j]=dist[u]+g.edges[u][j]
               path[j]=u
    DispAllPath(dist,path,S,v,g.n,g.b)	#输出所有最短路径及长度
def DispAllPath(dist,path,S,v,n,b):   	#输出从顶点v出发的所有最短路径
  for i in range(n):			#循环输出从顶点v到i的路径
    if S[i]==1 and i == b:
      apath=[]
      apath.append(i)			#添加路径上的终点
      k=path[i];
      if k==-1:			#没有路径的情况
         print("无路径")
      else:				#存在路径时输出该路径
         while k!=v:
            apath.append(k)		#顶点k加入到路径中
            k=path[k]
         apath.append(v)		#添加路径上的起点
         apath.reverse()            	#逆置apath
         print(*apath)               	#输出最短路径
         print(dist[i])
if __name__ == '__main__':
    #主程序
    g=MatGraph()
    g.CreateMatGraph()
    Dijkstra1(g,g.a)