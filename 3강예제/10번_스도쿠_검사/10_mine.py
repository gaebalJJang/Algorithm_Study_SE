a = [list(map(int, input().split())) for _ in range(9)]



for i in range(9):
    cnt = [0] * 9
    for j in range(9):
        print(a[i][j])
        if cnt[a[i][j]-1] == 0:
            cnt[a[i][j]-1] += 1
            
        else:
            print("NO")
            break
    cnt = [0] * 9
    for j in range(9):
        if cnt[a[j][i]-1] == 0:
            cnt[a[j][i]-1] += 1
        else:
            print("NO")
            break

print("YES")