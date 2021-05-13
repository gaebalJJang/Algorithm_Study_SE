n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
for i in range(m):
    h, t, k = map(int, input().split())
    if t==0:
        for _ in range(k):
            #pop 빼고 자동으로 땡겨짐
            #뺀 값을 맨 뒤로 넣어줌
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            #0번째 자리에 넣기
            a[h-1].insert(0, a[h-1].pop(0))

#모래시계 구하기
res = 0
s = 0
e = n-1
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else :
        s -= 1
        e += 1

print(res)