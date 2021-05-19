n, m = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort()

lt = 0
rt = n-1

while lt <= rt:
    mid = (rt+lt)//2
    if (numbers[mid] == m):
        print(mid+1)
        break
    elif numbers[mid] > m:
        rt = mid - 1
    else :
        lt = mid + 1
    