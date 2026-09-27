n = int(input())
employee_ids = list(map(int, input().split()))

if len(employee_ids) != n:
	print("Invalid input")
elif len(employee_ids) == len(set(employee_ids)):
	print("YES")
else:
	print("NO")
