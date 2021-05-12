n = int(input())
#리스트를 n개 받아서 2차원 배열에 넣는 방법
a = [list(map(int, input().split())) for _ in range(n)]
print(a)

s = e = n//2
row = 0
res = 0

while row <= n//2 :
    
    for i in range(s, e+1):
        print(row, i)
        res += a[row][i]
    s -= 1
    e += 1
    row += 1

while row < n :
    for i in range(s, e+1):
        
        res += a[row][i]
    s += 1
    e -= 1
    row += 1

print(res)