n, m = map(int, input().split())

visited = []
cnt = 0
def solution():
    global cnt
    if len(visited) == m:
        for x in visited:
            print(x, end=" ")
        print()
        cnt += 1
        return
    else:
        for i in range(1, n+1):
            if len(visited) == 0 or visited[-1] < i:
                visited.append(i)
                solution()
                visited.pop()
        
solution()
print(cnt)