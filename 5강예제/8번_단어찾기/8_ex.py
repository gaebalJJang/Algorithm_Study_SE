n = int(input())
#딕셔너리 : 문자를 index로 가질 수 있음
p = dict()
#단어를 key로 하고 val를 모두 1로 한다음에
for i in range(n):
    word = input()
    p[word] = 1
#해당되는 단어가 있으면 0으로 바꿈
for i in range(n-1):
    word = input()
    p[word] = 0

#p돌면서 value가 1인 key 출력
for key, val in p.items():
    if val == 1:
        print(key)
        break
