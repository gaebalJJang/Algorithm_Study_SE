num, m = map(int, input().split())
#num을 리스트로 
num = list(map(int, str(num)))

stack = []
for x in num:
    # stack이 비어있지 않고, m(제거할 자릿수)이 0보다 크고, 스택의 마지막 숫자가 현재 숫자보다 작으면 pop
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)

#다 지우지 못한 경우
if m != 0 :
    #뒤에서 m개 잘라냄
    stack = stack[:-m]

#리스트 한 줄로 붙여주기
res = ''.join(map(str, stack))
print(res)

# for x in stack:
#     print(x, end='')