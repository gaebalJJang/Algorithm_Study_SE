n = int(input())
a = list(map(int, input().split()))

seq = [0] * n

for i in range(n):
    #j: seq 훑으면서 빈공간 있으면 들어가기
    for j in range(n):
        #a[i]가 0되면 ㄲ
        if a[i]==0 and seq[j]==0:
            seq[j] += i+1
            break
        #아직 자릿수 못채움 a[i] 줄이고 j 늘어남
        elif seq[j]==0:
            a[i]-=1

for x in seq:
    print(x, end=' ')