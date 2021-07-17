import sys
input = sys.stdin.readline

def DFS(v, sum):
    if sum > n:
        return
    if v == m:
        global res
        if sum <= 259 and sum > res:
            res = sum
    else: 
        DFS(v+1, sum + W[v])
        DFS(v+1, sum)

n, m = map(int, input().split())
W = []
for _ in range(m):
    W.append(int(input()))
res = 0
DFS(0, 0)
print(res)