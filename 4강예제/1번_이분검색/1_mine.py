n, m = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

for idx, val in enumerate(numbers):
    if val == m:
        print(idx + 1)