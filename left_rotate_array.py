arr = [1, 2, 3, 4, 5]
d =2
n = len(arr)
d = d%n

left = 0
right = n-1

while left<right:
  arr[left],arr[right]=arr[right],arr[left]
  left+=1
  right-=1


left = 0
right = d-1

while left<right:
  arr[left],arr[right]=arr[right],arr[left]
  left+=1
  right-=1

left = d
right = n-1

while left<right:
  arr[left],arr[right]=arr[right],arr[left]
  left+=1
  right-=1

print(arr)