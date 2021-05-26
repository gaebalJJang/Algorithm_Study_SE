n, m = map(int, input().split())
weight = list(map(int, input().split()))

weight.sort()

for i in range(n):
    if (weight[i] + weight[n-i-1]) > m:
        