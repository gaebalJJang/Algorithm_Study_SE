board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

#i : 시작점, 5개짜리 회문수 구하므로 3까지만
for i in range(3):
    for j in range(7):
        #행 내에서 검사
        #i가 0이면 0~4까지를 tmp로 분리
        tmp=board[j][i:i+5]
        #역순비교
        if tmp==tmp[::-1]:
            cnt += 1

        #열 내에서 검사 : slice 쓸 수 없음
        for k in range(2):
            #길이가 5개이므로 2번만 검사하면 됨
            if board[i+k][j]!=board[i+5-k-1][j]:
                break
        else:
            cnt += 1
        