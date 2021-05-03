n, k = map(int, input().split())

#k번째를 확인할 카운트 변수
cnt = 0

for i in range(1, n+1):
    if n%i == 0:
        cnt +=1
    if cnt == k:
        print(i)
        break
else:
#for문이 정상적으로 다 돌았을 경우
#즉, k번째 약수가 없는 경우
    print(-1)