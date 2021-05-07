n = int(input())
num = list(map(int, input().split()))

def reverse(x):
  temp = []
  res = 0

  #1의자리부터 리스트로 넣기
  while x > 0:
    temp.append(x%10)
    x = int(x/10)

    #한자리수일때 오륲

  #10 곱하고 다음 자리 더하고 반복
  res = temp[0] * 10 + temp[1]
  for i in range(2, len(temp)):
    res = res * 10 + temp[i]
  return res

def isPrime(x):
  #소수이면 True, 아니면 False
  res = False
  for i in range(2, x):
    if x%i == 0:
      res = False
      break
    else:
      res = True
  return res

for i in range(n):
  rev = reverse(num[i])
  if isPrime(rev) == True:
    print(rev)