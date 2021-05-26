from collections import deque
n = map(int, input().split())
num = list(map(int, input().split()))

res = []
resnum = []

num = deque(num)

if num[0] < num[-1]:
    resnum.append(num[0])
    res.append('L')
    num.popleft()
else:
    resnum.append(num[-1])
    res.append('R')
    num.pop()

while num:
    if num[0] > resnum[-1] and num[-1] > resnum[-1]:
        if num[0] < num[-1]:
            resnum.append(num[0])
            res.append('L')
            num.popleft()
        else:
            resnum.append(num[-1])
            res.append('R')
            num.pop()
    elif num[0] > resnum[-1]:
        resnum.append(num[0])
        res.append('L')
        num.popleft()
    elif num[-1] > resnum[-1]:
        resnum.append(num[-1])
        res.append('R')
        num.pop()
    else:
        break

for i in res:
    print(i, end="")