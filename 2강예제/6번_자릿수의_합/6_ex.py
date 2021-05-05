
def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10
        x=x//10
    return sum

n=int(input())
a=list(map(int, input().split()))
res=0
#가장 작은 정수
max=-2147000000
for x in a:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x
print(res)