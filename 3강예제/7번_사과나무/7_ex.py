n = int(input())
#리스트를 n개 받아서 2차원 배열에 넣는 방법
a = [list(map(int, input().split())) for _ in range(n)]

res = 0
s = e = n//2

for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(res)