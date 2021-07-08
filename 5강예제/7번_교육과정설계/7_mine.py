must = list(input())
line = int(input())

res = []

#line번 반복
for _ in range(line):
    ex = list(input())
    temp = []
    #문장 돌면서 must에 포함되면 append / 중복 되는 거 있으면 넣지 않음
    for i in ex:
        if i in must and i not in temp:
            temp.append(i)

# 중복 제거한 뒤 넣었을 때 must랑 같으면 순서가 같게 들어간 것 == YES
    if temp == must:
        res.append("YES")
    else:
        res.append("NO")
    
for x in range(len(res)):
    print(res[x])