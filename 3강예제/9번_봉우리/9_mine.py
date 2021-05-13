n = int(input())
#리스트를 n개 받아서 2차원 배열에 넣는 방법
a = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

for i in range(n+1):
    for j in range(n+1):
        #a[i][j]
