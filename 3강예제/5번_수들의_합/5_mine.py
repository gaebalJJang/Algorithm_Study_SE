n, m = map(int, input().split())
num = list(map(int, input().split()))

cnt = 0
for i in range(0, n-1):
    sum = num[i]
    for j in range(i+1, n):
        sum += num[j]
        if sum == m:
            cnt += 1
    

print(cnt)