arr = list(map(int, input().split()))

odd_sum = 0
odd_count = 0
even_sum = 0
even_count = 0

for num in arr:
	if num % 2 == 0:
		even_sum += num
		even_count += 1
	else:
		odd_sum += num
		odd_count += 1

odd_average = odd_sum / odd_count if odd_count else 0
even_average = even_sum / even_count if even_count else 0

print("Average of odd numbers:", odd_average)
print("Average of even numbers:", even_average)
