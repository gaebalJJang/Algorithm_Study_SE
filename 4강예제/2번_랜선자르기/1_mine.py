k, n = map(int, input().split())

length = []

for i in range(k):
    x = int(input())
    length.append(x)

max = max(length)

lt = 0
rt = max

res = 0

while lt <= rt:
    mid = (lt+rt)//2
    num = 0
    for i in length:
        num += i // mid
    if num >= n:
        #어차피 lt, rt가 있으니까 이 if조건은 없어도 됐다..!
        if mid > res:
            res = mid
            lt = mid+1
        else:
            break
    else:
        rt = mid-1

print(res)