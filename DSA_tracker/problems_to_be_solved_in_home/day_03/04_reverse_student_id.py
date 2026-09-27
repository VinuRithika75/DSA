student_id = input().strip()

if not student_id:
	print("Invalid input")
else:
	reversed_id = ""

	for i in range(len(student_id) - 1, -1, -1):
		reversed_id += student_id[i]

	print(reversed_id)
