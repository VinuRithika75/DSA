
arr = list(map(int, input().split()))

largest = arr[0]
second = arr[1]

large_index = 0
second_index = 1

for i in range(2, 5):
    if arr[i] > largest:
        second = largest
        second_index = large_index
        largest = arr[i]
        large_index = i

    elif arr[i] > second:
        second = arr[i]
        second_index = i

print("Largest:", largest)
print("Index:", large_index)
print("Second largest:", second)
print("Index:", second_index)