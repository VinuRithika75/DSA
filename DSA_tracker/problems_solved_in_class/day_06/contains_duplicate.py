n = int(input())
arr = list(map(int, input().split()))

seen = set()
contains_duplicate = False

for i in range(n):
	if arr[i] in seen:
		contains_duplicate = True
		break

	seen.add(arr[i])

print(contains_duplicate)
