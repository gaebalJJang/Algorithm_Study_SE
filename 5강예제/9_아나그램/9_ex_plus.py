a = input()
b = input()

sH = dict()

for x in a:
    sH[x] = sH.get(x, 0) + 1

for x in b:
    sH[x] = sH.get(x, 0) - 1

for x in sH.keys():
    if sH[x] != 0:
        print("NO")
        break
else:
    print("YES")