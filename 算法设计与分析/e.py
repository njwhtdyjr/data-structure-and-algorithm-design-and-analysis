from random import uniform
n=int(input())
cnt=0
for i in range(1,n+1):
    x=uniform(1,2)
    y=uniform(0,1)
    if y<1/x:
        cnt+=1
e=2**(n/cnt)
print(e)
