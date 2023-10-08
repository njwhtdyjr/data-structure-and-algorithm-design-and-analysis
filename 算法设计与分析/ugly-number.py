ugly = [1]

i = 0
j = 0
k = 0
n = int(input())

while len(ugly) < n:
    t = min(min(ugly[i] * 2, ugly[j] * 3), ugly[k] * 5)
    ugly.append(t)
    if ugly[i]*2 == t:
        i += 1
    if ugly[j]*3 == t:
        j += 1
    if ugly[k]*5 == t:
        k += 1


print(ugly[n-1])
















