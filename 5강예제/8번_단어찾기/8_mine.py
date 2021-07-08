num = int(input())

#wordList에 단어 다 넣고 for문 돌리면서 wordlist에 있으면 remove
#젤 마지막에 남은 거 출력
wordList = []
for _ in range(num):
    wordList.append(input())

for _ in range(num-1):
    word = input()
    if word in wordList:
        wordList.remove(word)
    
print(wordList[0])