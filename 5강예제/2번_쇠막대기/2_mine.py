#강의 듣고 풀어보기
bracket = list(input())
stack = []
sum = 0

for x in range(len(bracket)):
    if bracket[x] == "(":
        stack.append(bracket[x])
    else:
        #")"
        if bracket[x-1] == "(":
            #레이저
            stack.pop()
            sum += len(stack)
        else:
            #))
            stack.pop()
            sum += 1

print(sum)

