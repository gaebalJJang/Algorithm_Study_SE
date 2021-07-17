import sys 

def DFS(v):
    if v == n:
        total1 = 0
        total2 = 0
        for i in range(n):
            if ch[i] == 1:
                total1 += numbers[i]
            else:
                total2 += numbers[i]
        else:
            if total1 == total2:
                print('YES')
                sys.exit(0)
    else:
        ch[v] = 1
        DFS(v+1)
        ch[v] = 0
        DFS(v+1)

n = int(input())
numbers = list(map(int, input().split()))
ch = [0] * n
DFS(0)
print("NO")
