n = int(input())
#리스트를 n개 받아서 2차원 배열에 넣는 방법
a = [list(map(int, input().split())) for _ in range(n)]

m = int(input())


def rotate(list, r, num):
    for _ in range(num):
        for i in range(n):
            if r == 0:
                if i == n:
                    list[i] = list[0]
                else:
                    list[i] = list[i+1]
            else:
                if i == 0:
                    list[i] = list[n-1]
                else:
                    list[i] = list[i-1]
    return list

for i in range(m):
    order = list(map(int, input().split()))
    a[order[0]] = rotate(list[order[0]], order[1], order[2])

print(a)