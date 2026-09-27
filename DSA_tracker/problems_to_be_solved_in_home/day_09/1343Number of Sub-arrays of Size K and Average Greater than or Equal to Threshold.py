class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        target_sum = threshold * k
        
        
        current_sum = 0
        for i in range(k):
            current_sum += arr[i]
            
        count = 1 if current_sum >= target_sum else 0
        
        
        for i in range(k, len(arr)):
            current_sum += arr[i] - arr[i - k]
            if current_sum >= target_sum:
                count += 1
                
        return count