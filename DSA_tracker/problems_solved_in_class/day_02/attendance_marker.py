t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))

    absent = 0

    for i in arr:
        if i == 0:
            absent += 1

    print(absent)