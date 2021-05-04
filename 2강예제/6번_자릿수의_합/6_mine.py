n = int(input())
num = list(map(int, input().split()))

def digit_sum(x):
  sum = 0
  #자릿수를 다 더한다
  while x>0 :
    sum = sum + (x%10)
    x = int(x/10)
    
  return sum

max = 0
res = 0

#자릿수를 다 더한 값의 최대값을 구한다
for idx, x in enumerate(num):
  if digit_sum(x) > max:
    max = digit_sum(x)
    res = x

print(res)
