n = int(input())

arr = list(map(int, input().split()))
index = list(map(int, input().split()))

result = [0] * n

for i in range(n):
    result[index[i]] = arr[i]

for i in range(n):
    print(result[i], end=" ")