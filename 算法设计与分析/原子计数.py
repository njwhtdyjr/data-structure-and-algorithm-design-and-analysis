formula = input()
stack = []
i = 0
n = len(formula)
dic = {}

while i < n:
    c = formula[i]
    i += 1

    if c == '(':
        stack.append('(')
    elif c == ')':
        num = 0
        while i < n and formula[i].isdigit():
            num = num * 10 + int(formula[i])
            i += 1
        if num == 0:
            num = 1
        temp = {}
        dic1 = {}
        while stack and stack[-1] != '(':
            elem = stack.pop()
            temp[elem[0]] = temp.get(elem[0],0)+elem[1]
        stack.pop()
        for key,value in temp.items():
            dic1[key] = dic1.get(key,0)+value*num
        for key,value in dic1.items():
            stack.append([key,value])
    elif c.isdigit():
        num = int(c)
        while i < n and formula[i].isdigit():
            num = num * 10 + int(formula[i])
            i += 1
        stack[-1][1] += num - 1
    elif c.isupper():
        elem = c
        while i < n and formula[i].islower():
            elem += formula[i]
            i += 1
        stack.append([elem,1])
for item in stack:
    if item[0] in dic:
        dic[item[0]] += item[1]
    else:
        dic[item[0]] = item[1]

list = []
for key,value in dic.items():
    list.append([key,value])
list.sort(key = lambda x:x[0])

dic2 = {}
for item in list:
    dic2[item[0]] = item[1]
print(dic2)
