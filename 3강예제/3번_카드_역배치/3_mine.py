card = []
for i in range(20):
    card.append(i+1)

for i in range(10):
    n, m = map(int, input().split())
    temp = card[n-1:m]
    cnt = 0
    for j in range(m-1, n-2, -1):
        card[j] = temp[cnt]
        cnt += 1

    
for i in card:
    print(i, end=' ')