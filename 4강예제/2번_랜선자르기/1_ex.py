#len: 랜선 길이
#몇개의 랜선을 만들 수 있는지 계산하는 함수
def Count(len):
    cnt=0
    for x in Line:
        cnt+=(x//len)
    return cnt

k, n=map(int, input().split())
Line=[]
res=0
largest=0
for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    #largest랑 tmp중에 큰 값을 저장
    largest=max(largest, tmp)
lt=1
rt=largest
#본격계산
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=n:
        #mid 가능함
        res=mid
        #더 좋은 값을 찾아보자
        lt=mid+1
    else:
        rt=mid-1
print(res)