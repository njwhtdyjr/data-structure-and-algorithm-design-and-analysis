def evalRPN(strexp):
    lis = strexp.split()
    stack = []
    for i in lis:#如果是数字就进栈
        if i.isdigit() or len(i)>1 :
            stack.append(int(i))
        else:#如果不是数字就取出栈顶的两个元素
            a = stack.pop()
            b = stack.pop()
            c = eval(str(b)+i+str(a))
            stack.append(int(c))
    return stack.pop()
strexp = input()
print(evalRPN(strexp))




