l = int(input())
val = list(map(int, input().split()))
m = int(input())

for i in range(m):
    maxi = val.index(max(val))
    mini = val.index(min(val))
    val[maxi] -= 1
    val[mini] += 1

print(max(val)-min(val))
