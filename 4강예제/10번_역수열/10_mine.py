n = int(input())
num = list(map(int, input().split()))

res = []

for i in range(1, n+1):
    cnt = 0
    x = num.index(i)
    tmp = num[0:x]
    for j in tmp:
        if j > i:
            cnt += 1
    res.append(cnt)

for i in res:
    print(i, end=" ")
    