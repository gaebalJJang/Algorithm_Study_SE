from collections import deque
need = input()
n = int(input())

for i in range(n):
    plan = input()
    dq = deque(need)
    #list 안해줘도 되넹...
    for x in plan:
        if x in dq:
            if x != dq.popleft()
                print("#%d NO" %(i+1))
                break
    #for문 다 돌았을 시 
    #순서는 다 맞으나 dq에 남아있는 게 있으면 빼먹은거라 안됨
    else:
        if len(dq) == 0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))