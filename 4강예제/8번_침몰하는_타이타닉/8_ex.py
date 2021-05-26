from collections import deque
n, limit = map(int, input().split())
p = list(map(int, input().split()))

p.sort()
#앞 뒤로 pop연산이 다 가능한 자료구조
p = deque(p)
cnt = 0

#p가 비어있으면 멈춤
while p:
    #마지막 한명 남으면
    if len(p) == 1:
        cnt += 1
        break
    #무게 안되면 혼자 타고
    if p[0] + p[-1] > limit:
        p.pop()
        cnt += 1
    #되면 둘 다 타고
    else:
        p.popleft()
        p.pop()
        cnt += 1

print(cnt)