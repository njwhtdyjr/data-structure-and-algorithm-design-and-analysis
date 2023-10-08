def intersection(a,b):
    c = len(a)
    d = len(b)
    if c == 1 and d != 1:
        return intersection(a,b[0:int(d/2)])+intersection(a,b[int(d/2):])
    if c != 1 and d == 1:
        return intersection(a[0:int(c/2)],b)+intersection(a[int(c/2):],b)
    if c == 1 and d == 1:
        if a[0] == b[0]:
            return [a[0]]
        else: return []
    if a[int(c/2)-1] < b[int(d/2)]:
        return intersection(a[0:int(c/2)],b[0:int(d/2)])+intersection(a[int(c/2):],b[0:int(d/2)])+intersection(a[int(c/2):],b[int(d/2):])
    else:
        return intersection(a[0:int(c/2)],b[0:int(d/2)])+intersection(a[0:int(c/2)],b[int(d/2):])+intersection(a[int(c/2):],b[int(d/2):])
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
d = list(map(int,input().split()))


print(intersection(intersection(a,b),intersection(c,d)))