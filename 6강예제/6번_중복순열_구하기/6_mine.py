import sys
input = sys.stdin.readline

def solution(v):
    global cnt
    if v == m:
        for x in ch:
            print(x, end=" ")
        cnt += 1
        print()

    else:
        for i in range(1, n+1):
            ch[v] = i
            solution(v+1)


n, m = map(int, input().split())
cnt = 0
ch = [0] * m
solution(0)
print(cnt)
