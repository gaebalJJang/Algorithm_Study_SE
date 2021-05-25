n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e)) #튜플 형태로 넣기
#끝나는 시간을 정렬 x[1]을 먼저
#그냥 sort하면 앞에꺼 먼저 정렬함 순서대로
#이거 솔직히 못 쓸거같다 ㅎ헤
meeting.sort(key=lamda x : (x[1], x[0]))

#끝나는 시간
et = 0
cnt = 0
for s, e in meeting:
    if s>=et:
        et = e
        cnt += 1
    
print(cnt)