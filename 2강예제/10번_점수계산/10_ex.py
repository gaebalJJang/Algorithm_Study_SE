
n=int(input())
a=list(map(int, input().split()))
cnt=0
sum=0

#for문 형태 리스트 안의 데이터로 바로 접근
for i in range(n):
    if a[i]==1:
        cnt=cnt+1
        sum=sum+cnt
    else:
        cnt=0

print(sum)