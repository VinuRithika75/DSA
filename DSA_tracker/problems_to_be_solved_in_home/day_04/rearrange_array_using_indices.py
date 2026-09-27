arr = [10, 11, 12]
index = [1, 0, 2]

n = len(arr)

result = [0] * n

for i in range(n):
    result[index[i]] = arr[i]

print(result)