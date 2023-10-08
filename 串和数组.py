n = int(input())
matrix = []
for i in range(n):
  lis = list(map(int,input().split()))
  matrix.append(lis)
#存储矩阵



#旋转函数
def rotate(matrix):
    n = len(matrix)#将矩阵中的元素一层一层地旋转，j代表层数
    for j in range(n//2):#i表示第j层中需要旋转的次数，每次旋转交换四个数的位置
        for i in range(n-1-2*j):
            matrix[j][i+j],matrix[i+j][-1-j],matrix[-1-j][-1-i-j],matrix[-1-i-j][j] = matrix[-1-i-j][j],matrix[j][i+j],matrix[i+j][-1-j],matrix[-1-j][-1-i-j]

rotate(matrix)

#输出部分
for row in matrix:
    print(*row)