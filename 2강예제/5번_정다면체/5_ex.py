n, m = map(int, input().split())
#개수 셀 빈 배열 생성
cnt = [0]*(n+m+1)
max = -555

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j]+=1

for i in range(n+m+1):
    if cnt[i]>max:
        max=cnt[i]

for i in range(n+m+1):
    if cnt[i] == max:
        print(i, end=" ")