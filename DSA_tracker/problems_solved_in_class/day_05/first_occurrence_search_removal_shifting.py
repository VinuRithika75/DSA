n = int(input())
arr = list(map(int, input().split()))
target = int(input())

first_index = -1

for i in range(n):
	if arr[i] == target:
		first_index = i
		break

if first_index != -1:
	for i in range(first_index, n - 1):
		arr[i] = arr[i + 1]

	n -= 1

print(*arr[:n])
