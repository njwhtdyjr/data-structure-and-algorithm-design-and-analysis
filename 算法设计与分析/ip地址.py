import copy
s = input()
res = ['']
i = 1
res2 = []
def divide(s,i):
    if i == 5:
        if len(s) > 0:
            res.pop()
            return False
        else:
            res2.append(res.pop()[:-1])
            return False
    if len(s) > 15 - 3*i or len(s) < 5 - i:
        res.pop()
        return False
    elif len(s) > 0:
            if s[0] == '0':
                temp = copy.deepcopy(res)
                print(temp)
                print(s)
                while len(res) != 0:
                    res.pop()
                for ip in temp:
                    res.append(ip + s[0] + '.')
                    divide(s[1:],i+1)
                del temp
            else:
                temp = copy.deepcopy(res)
                print(temp)
                print(s)
                while len(res) != 0:
                    res.pop()
                for ip in temp:
                    res.append(ip+s[0]+'.')
                    divide(s[1:],i+1)
                if len(s)>=2:
                    for ip in temp:
                        res.append(ip+s[0:2]+'.')
                        divide(s[2:],i+1)
                if len(s) >=3 and int(s[0:3]) <= 255:
                    for ip in temp:
                        res.append(ip+s[0:3]+'.')
                        divide(s[3:],i+1)
                del temp
divide(s,i)
for re in res:
    res2.append(re[:-1])
print(res2)
