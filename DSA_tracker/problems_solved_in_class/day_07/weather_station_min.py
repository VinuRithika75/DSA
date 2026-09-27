n = int(input())
arr = list(map(int, input().split()))

current_min = arr[0]

for temp in arr:
    if temp < current_min:
        current_min = temp

    print(current_min, end=" ")