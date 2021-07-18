import sys
input = sys.stdin.readline

def solution(v):
    global res
    if v == n:
        money = 0
        for i in range(n):
            money += ch[i] * coin[i]
        
        if money == charge:
            amnt = sum(ch)
            if amnt < res:
                res = amnt
    else:
        for i in range(res+1):
            ch[v] = i
            solution(v+1)

n = int(input())
coin = list(map(int, input().split()))
charge = int(input())
res = charge
ch = [0] * n
solution(0)

print(res)