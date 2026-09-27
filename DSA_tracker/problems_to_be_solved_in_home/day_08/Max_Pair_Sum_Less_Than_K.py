class Solution:
    def maxSum(self, arr, k):
     
               arr.sort()

               left = 0
               right = len(arr) - 1

               best = -1
               ans = [-1, -1]

               while left < right:
                   total = arr[left] + arr[right]

                   if total < k:

                       if total > best:
                           best = total
                           ans = [arr[left], arr[right]]

                       left += 1

                   else:
                       right -= 1

               return ans