n = int(input())
arr = list(map(int, input().split()))

current_max = arr[0]
current_min = arr[0]

for num in arr:

    if num > current_max:
        current_max = num

    if num < current_min:
        current_min = num

    current_range = current_max - current_min

    print(current_range, end=" ")