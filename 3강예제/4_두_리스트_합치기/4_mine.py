n = int(input())
first = list(map(int, input().split()))
m = int(input())
second = list(map(int, input().split()))


for i in second:
    first.append(i)

first.sort()

for i in first:
    print(i, end=' ')