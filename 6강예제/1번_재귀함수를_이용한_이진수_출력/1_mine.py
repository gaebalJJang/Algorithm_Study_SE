n = int(input())

def solution(input):
    if input > 0:
        x = input % 2
        solution(input // 2)
        print(x, end='')

solution(n)