import sys
input = sys.stdin.readline

n, f = map(int, input().split())

selected = []
def dfs():
    if len(selected) == n:
        sum = 0
        for i in range(n):
            sum += selected[i] * b[i]
        else:
            if sum == f:
                for x in selected:
                    print(x, end = " ")
                sys.exit(0)
    else:
        for i in range(1, n+1):
            if i not in selected or len(selected) == 0:
                selected.append(i)
                dfs()
                selected.pop()

b = [1] * n

for i in range(1, n):
    b[i] = b[i-1] * (n-i) // i

dfs()