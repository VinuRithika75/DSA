class Solution:
    def rearrange(self, arr):
        # code herearr = [1, 2, 3, 4, 5, 6]

                   n = len(arr)

                   max_element = 0

            
                   for i in range(n):
                       if arr[i] > max_element:
                           max_element = arr[i]

                   base = max_element + 1

                   left = 0
                   right = n - 1

                 
                   for i in range(n):

                       if i % 2 == 0:
                           
                           arr[i] = arr[i] + (arr[right] % base) * base
                           right -= 1

                       else:
                          
                           arr[i] = arr[i] + (arr[left] % base) * base
                           left += 1

                   
                   for i in range(n):
                       arr[i] = arr[i] // base

                   print(arr)