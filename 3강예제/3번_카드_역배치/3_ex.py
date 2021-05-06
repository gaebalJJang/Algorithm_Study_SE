#리스트에 1~20까지 넣기
a=list(range(21))

#대칭되는 위치의 값만 바꿔주면 된다..!!!!!
for _ in range(10):
    s, e=map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i]=a[e-i], a[s+i]
a.pop(0)
for x in a:
    print(x, end=' ')