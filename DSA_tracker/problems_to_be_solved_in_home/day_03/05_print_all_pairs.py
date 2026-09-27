n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    for j in range(i + 1, n):
        print("(%d,%d)" % (arr[i], arr[j]))