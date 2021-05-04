N, K = map(int, input().split())
num = list(map(int, input().split()))

#중복을 제거하는 자료구조
res = set()
for i in range(N):
    for j in range(i+1, N):
        for m in range(j+1, N):
            res.add(num[i] + num[j] + num[m])

#리스트로 바꿔줘야 소팅할 수 잇음
res = list(res)
#큰것부터 정렬
res.sort(reverse = True)
print(res[K-1])