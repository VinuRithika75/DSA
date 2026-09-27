try:
	n = int(input())
	arr = list(map(int, input().split()))

	if n <= 0 or len(arr) != n:
		print("Invalid input")
	else:
		print(*arr)

except ValueError:
	print("Invalid input")
