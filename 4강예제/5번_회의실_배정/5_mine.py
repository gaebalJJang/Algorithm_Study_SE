
n = int(input())

start = []
end = []

for i in range(n):
    x, y = map(int, input().split())
    start.append(x)
    end.append(y)

time = [0] * (max(end)+1)

res = 0

for i in range(n):
    print(i)
    cnt = 0
    for j in range(start[i], end[i]):
        time[j] = 1
    for k in range(i+1, n):
        print("k", k)
        temp = time[start[k]:end[k]]
        if (temp.count(1) == 0):
            
            print(temp)
            cnt += 1
    if cnt > res:
        res = cnt

print(res)

