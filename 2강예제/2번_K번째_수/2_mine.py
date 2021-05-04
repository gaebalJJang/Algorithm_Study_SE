t = int(input())

ouput = []

for i in range(0,t):

    n, s, e, k = map(int, input().split())
    num = list(map(int, input().split()))

    num.sort()

    print("#%d %d" %(i + 1,num[k-1]))