import heapq as hq
#heapq는 기본적으로 최소힙
#최소힙에 부호를 반대로 바꿔서 넣기

a = []
while True:
    n = int(input())
    if n == -1: #종료
        break
    if n == 0: #최소값 pop
        if len(a) == 0:
            print(-1)
        else:
            print(-hq.heappop(a))
    else:
        hq.heappush(a, -n)

