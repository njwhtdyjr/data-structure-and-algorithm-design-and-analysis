time_limited = list(map(float,input().split()))
time_actual = list(map(float,input().split()))

i = 0
N = len(time_limited)

while(i < N):
    time_left = 0
    for j in range(N):
        time_need = time_actual[(i+j)%N]
        time_left += time_limited[(i+j)%N] - time_need
        if time_left < 0:
            if i == N-1:
                print("无法完成正常配送")
                break
            break

        if j == N-1:
            print("能从配送点%d正常完成配送"%i)
            i = N
    i += 1

















