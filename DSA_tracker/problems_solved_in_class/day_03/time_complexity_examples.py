def constant_time(arr):
	return arr[0] if arr else None


def logarithmic_time(n):
	steps = 0

	while n > 1:
		n //= 2
		steps += 1

	return steps


def linear_time(arr):
	total = 0

	for num in arr:
		total += num

	return total


def quadratic_time(arr):
	pair_count = 0

	for _ in arr:
		for _ in arr:
			pair_count += 1

	return pair_count


try:
	n = int(input("Enter the size of the array: "))

	if n <= 0:
		print("Invalid input")
	else:
		arr = list(map(int, input("Enter the array elements: ").split()))

		if len(arr) != n:
			print("Invalid input")
		else:
			print("Constant time result:", constant_time(arr))
			print("Logarithmic time result:", logarithmic_time(n))
			print("Linear time result:", linear_time(arr))
			print("Quadratic time result:", quadratic_time(arr))

except ValueError:
	print("Invalid input")
