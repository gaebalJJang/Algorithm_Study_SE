t = int(input())

ouput = []

for i in range(0,t):

    n, s, e, k = map(int, input().split())
    num = list(map(int, input().split()))

    #s에서 e까지 자르기 slice 함수
    num = num[s-1: e]

    num.sort()

    print("#%d %d" %(i + 1,num[k-1]))