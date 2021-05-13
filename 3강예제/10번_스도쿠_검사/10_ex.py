ch = [0] * 10

def check(a):
    for i in range(9):
        ch1 = [0]*10
        ch2 = [0]*10
        for j in range(9):
            #행체크
            ch1[a[i][j]] = 1
            #열체크
            ch2[a[j][i]] = 1
        if sum(ch1)!=9 or sum(ch2)!=9 :
            return False
    #9개의 그룹
    for i in range(3):
        for j in range(3):
            ch3 = [0]*10
            #9개의 숫자
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]] = 1
            if sum(ch3)!=9:
                return False
    return True


a=[list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")
