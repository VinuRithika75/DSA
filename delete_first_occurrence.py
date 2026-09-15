n = int(input())

arr = list(map(int, input().split()))

ele = int(input())

index = -1

for i in range(n):
    if arr[i] == ele:
        index = i
        break

if index != -1:
    for i in range(index, n - 1):
        arr[i] = arr[i + 1]

    n = n - 1

for i in range(n):
    print(arr[i], end=" ")