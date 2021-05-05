string = str(input())

num = 0
cnt = 0

for i in string:
    if i.isdecimal():
        num = num * 10 + int(i)

for i in range(1, num+1):
    if num % i == 0:
        cnt += 1

print(num)
print(cnt)