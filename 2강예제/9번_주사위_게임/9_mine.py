n = int(input())

def money(list):
    res = 0
    max = 0

    for i in range(3):
        if list[i] > max:
            max = list[i]

    if (list[0]==list[1]==list[2]):
        res = 10000+max*1000
    elif (list[0]==list[1] or list[1]==list[2] or list[2]==list[0]):
        res = 1000+max*100

    else:
        res = max*100

    return res

max = 0
for i in range(n):
    dice = list(map(int, input().split()))
    if money(dice) > max:
        max = money(dice)

print(max)
