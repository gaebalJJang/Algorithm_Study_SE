import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [[0] * n for i in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    matrix[x-1][y-1] = 1

visited = [0]
cnt = 0
def dfs(last):
    global cnt
    if last == n-1:
        cnt += 1
        return
    else:
        for i in range(n):
            if i not in visited and matrix[last][i] == 1:
                visited.append(i)
                dfs(i)
                visited.pop()
    
dfs(0)
print(cnt)