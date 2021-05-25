n = int(input())

player = []
res = n

for _ in range(n):
    h, w = map(int, input().split())
    player.append((h, w))

player.sort()

for i in range(n):
    for j in range(i+1, n):
        if player[j][1] > player[i][1]:
            res -= 1
            break

print(res)
