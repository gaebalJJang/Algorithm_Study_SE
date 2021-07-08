num = int(input())

wordList = []
for _ in range(num):
    wordList.append(input())

for _ in range(num-1):
    word = input()
    if word in wordList:
        wordList.remove(word)
    
print(wordList[0])