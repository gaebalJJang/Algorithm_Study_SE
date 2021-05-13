#2차원배열의 상하좌우를 얻기 위한 장치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

#가장자리를 0으로 초기화
#0번 행에 n개의 0이 들어간 행 insert
a.insert(0, [0]*n)
#맨 밑 행에 n개의 0이 들어간 행 append
a.append([0] * n)

#각각의 행에 앞 뒤에 0 넣기
for x in a:
    x.insert(0, 0)
    x.append(0)

cnt = 0
#상하좌우 확인
for i in range(1, n+1):
    for j in range(1, n+1):
        #all + for문: 모든게 참일때 참이됨
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1

print(cnt)
