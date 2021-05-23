n, c = map(int, input().split())
loc = []

for _ in range(n):
    x = int(input())
    loc.append(x)

loc.sort()

lt = 1
rt = loc[n-1]

def Count(len):
    cnt = 1
    ep = loc[0]
    for i in range(1, n):
        #처음 말과 현재 놓는 말과의 거리
        if loc[i]-ep >= len:
            cnt += 1
            ep = loc[i]
    return cnt


while lt <= rt:
    mid = (lt+rt)//2
    #Count 함수 : mid가 최대 거리일 때 배치할 수 있는 말의 수
    if Count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)