arr = list(map(int, input().split()))

minimum = arr[0]
maximum = arr[0]

for num in arr[1:]:
	if num < minimum:
		minimum = num

	if num > maximum:
		maximum = num

print("Minimum:", minimum)
print("Maximum:", maximum)
