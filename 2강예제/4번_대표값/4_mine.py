n = int(input())
score = list(map(int, input().split()))

#avg = round(sum(a)/n)
#round 함수는 round_half_even 방식
avg = sum(a)/n
avg = avg + 0.5
avg = int(avg)

ans = 10000
num = -1

for i in range(n):
    diff = abs(score[i]-avg)
    if diff == ans:
        if score[i] > score[num]:
            num = i
    
    elif diff < ans:
        num = i
        ans = diff

print(avg, num + 1)
    