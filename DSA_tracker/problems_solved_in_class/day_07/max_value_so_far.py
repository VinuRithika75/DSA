arr = [2, 5, 1, 8, 3]

current_max = arr[0]

for num in arr:
    if num > current_max:
        current_max = num

    print(current_max, end=" ")