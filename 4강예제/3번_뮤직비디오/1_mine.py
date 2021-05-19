n, m = map(int, input().split())
minutes = list(map(int, input().split()))

dvd = []

for i in range(1, n-m):
    div = i
    for k in range(m):
        