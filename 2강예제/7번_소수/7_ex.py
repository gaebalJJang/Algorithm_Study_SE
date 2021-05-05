#에라토스테네스 체 방법
#리스트를 만들고 정수의 배수를 제외하는 방법
n=int(input())
ch=[0]*(n+1)
cnt=0
for i in range(2, n+1):
    if ch[i]==0:
        cnt+=1
        for j in range(i, n+1, i):
            ch[j]=1
print(cnt)