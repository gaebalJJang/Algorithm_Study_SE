import sys
input = sys.stdin.readline

n, k = map(int, input().split())
numbers = list(map(int, input().split()))
m = int(input())

selected = []
cnt = 0
def solution():
    global cnt
    if len(selected) == k:
        if sum(selected) % m == 0:
            cnt += 1
        return
    else:
        for x in numbers:
            if len(selected) == 0 or selected[-1] < x:
                selected.append(x)
                solution()
                selected.pop()

solution()
print(cnt)