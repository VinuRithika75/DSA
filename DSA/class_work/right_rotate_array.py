n = int(input())
arr = list(map(int, input().split()))

d = int(input())

d = d % n

for _ in range(d):
    last = arr[n - 1]

    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = last

for i in range(n):
    print(arr[i], end=" ")