import heapq as hq
a = []
while True:
    n = int(input())
    if n == -1: #종료
        break
    if n == 0: #최소값 pop
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)
