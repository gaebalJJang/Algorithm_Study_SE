p, q=map(int, input().split())

data = []

for i in range(1,p+1) :
  if (p % i) == 0 :
    data.append(i)

print(data[q-1])