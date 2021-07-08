from collections import deque
n, m = map(int, input().split())

#튜플로 값이 들어감 = list 생성식
#pos: 위치 자동으로 들어감
#Val: input 값 list 형태로 받아서 넣음
Q = [(pos, Val) for pos, val in enumerate(list(map(int, input().split())))]
Q = deque(Q)

while True:
    cur = Q.popleft()
    #cur = (0, 30) //
    #cur[0] = 0, cur[1] = 30
    #Q안의 x를 돌면서 x[1]과 cur[1]을 비교
    if any(cur[1]<x[1] for x in Q):