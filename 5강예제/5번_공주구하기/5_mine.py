from collections import deque
princeNum, num = map(int, input().split())

prince = deque()

for x in range(1, princeNum + 1):
    prince.append(x)

while len(prince) > 1:
    for _ in range(num-1):
        temp = prince.popleft()
        prince.append(temp)
    prince.popleft()
    
print(prince.pop())