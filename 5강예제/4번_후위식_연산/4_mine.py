exp = input()
stack = []

for x in exp:
    if x.isdecimal():
        stack.append(int(x))
    else:
        num2 = stack.pop()
        num1 = stack.pop()
        if x == '+':
            res = num1 + num2
        elif x == '*':
            res = num1 * num2
        elif x == '/':
            res = num1 / num2
        elif x == '-':
            res = num1 - num2

        stack.append(res)

print(stack.pop())