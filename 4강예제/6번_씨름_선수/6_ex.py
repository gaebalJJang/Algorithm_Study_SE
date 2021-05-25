n = int(input())

body=[]

for i in range(n):
    a, b = map(int, input().split())
    body.append((a, b))

#키 큰 순으로 정렬, 몸무게 최대값을 저장하고 몸무게 최대가 갱신될 때 카운트
body.sort(reverse = True)
largest = 0
cnt = 0
for x, y in body:
    if y > largest:
        largest = cnt
        cnt += 1