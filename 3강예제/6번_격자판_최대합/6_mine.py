n = int(input())
num = []
max = 0

for i in range(n):
  row = list(map(int, input().split()))
  num.append(row)

#행
for i in range(n):
  x = sum(num[i])
  if x > max:
    max = x

#열
for i in range(n):
  x = 0
  for j in range(n):
    x += num[j][i]
  if x > max:
    max = x

#대각선
x = 0
for i in range(n):
  x += num[i][n - i - 1]
  if x > max:
    max = x

x = 0
for i in range(n):
  x += num[i][i]
  if x > max:
    max = x

print(x)