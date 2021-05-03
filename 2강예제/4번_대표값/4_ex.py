n = int(input())
a = list(map(int, input().split()))


#avg = round(sum(a)/n)
#round 함수는 round_half_even 방식
avg = sum(a)/n
avg = avg + 0.5
avg = int(avg)

min = 214000000

#idx키, x값
for idx, x in enumerate(a):
    tmp = abs(x-avg)

    if tmp<min:
        min = tmp
        #점수
        score = x
        #번호
        res = idx+1
    elif tmp == min:
        if x > score:
            score = x
            res = idx+1
print(avg, res)