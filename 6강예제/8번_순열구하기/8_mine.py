n, m = map(int, input().split())

visited = []
cnt = 0
def solution():
    global cnt
    if len(visited) == m:
        for x in visited:
            print(x, end=" ")
        cnt += 1
        print()
        return
    else:
        for i in range(1, n+1):
            if i not in visited:
                visited.append(i)
                solution()
                visited.pop()
solution()

print(cnt)