n = int(input())

arr = list(map(int, input().split()))

target = int(input())

left = 0
right = n - 1

best_diff = float('inf')
best_left = 0
best_right = n - 1

while left < right:

    current_sum = arr[left] + arr[right]
    current_diff = abs(current_sum - target)

    if current_diff < best_diff:
        best_diff = current_diff
        best_left = left
        best_right = right

    if current_sum < target:
        left += 1

    elif current_sum > target:
        right -= 1

    else:
        break

best_sum = arr[best_left] + arr[best_right]

print("Pair:", arr[best_left], arr[best_right])
print("Sum:", best_sum)
print("Difference:", best_diff)