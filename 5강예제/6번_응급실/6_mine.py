from collections import deque
n, m = map(int, input().split())
perc = list(map(int, input().split()))

dperc = deque()

#m번째 환지를 확인하기 위해 idx를 붙여줌
for i in range(len(perc)):
    dperc.append((perc[i], i))

#진료 순서
count = 0

#dperc를 계속 돌면서 맨 처음 게 가장 큰 숫자이면 count++ 하고 popleft, 
#아니면 popleft 해서 다시 맨 뒤로 append
#가장 큰 순서여서 popleft 된 애가 m번째 환자이면 break
while dperc:
    if dperc[0] == max(dperc):
        count += 1
        x = dperc.popleft()
        if x[1] == m:
            break
    else:
        x = dperc.popleft()
        dperc.append(x)

print(count)
