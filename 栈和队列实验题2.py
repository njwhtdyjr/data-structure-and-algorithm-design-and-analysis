

def GetNextval(t,nextval):	#由模式串t求出nextval值
  j,k=0,-1
  nextval[0]=-1
  while j<len(t)-1:
    if k==-1 or t[j]==t[k]:
      j,k=j+1,k+1
      if t[j]!=t[k]:
        nextval[j]=k
      else:			#t[j]=t[k]
        nextval[j]=nextval[k]
    else: k=nextval[k]

def KMPval(s,t):                       	#改进后的KMP算法
  nextval=[None]*len(t)
  GetNextval(t,nextval)			#求nextval数组
  i,j=0,0
  count = 0
  while i<len(s):
      while i<len(s) and j<len(t):
        if j==-1 or s[i]==t[j]:
          i,j=i+1,j+1             		#i,j各增1
        else: j=nextval[j] 		    	#i不变,j回退
      if j>=len(t):
         count += 1	    		#返回起始序号
         j = 0
  return count





if __name__ == '__main__':
    s=input() # 读入s串
    t=input() # 读入t串

    print(KMPval(s,t))