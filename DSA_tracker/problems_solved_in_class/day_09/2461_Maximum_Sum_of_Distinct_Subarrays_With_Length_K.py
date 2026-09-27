class Solution(object):
    def maximumSubarraySum(self, nums, k):
        max_sum = 0
        current_sum = 0
        freq_map = {}
        left = 0
        
        for right in range(len(nums)):
            num = nums[right]
            
            
            current_sum += num
            freq_map[num] = freq_map.get(num, 0) + 1
            
     
            if right - left + 1 > k:
                left_num = nums[left]
                current_sum -= left_num
                freq_map[left_num] -= 1
                if freq_map[left_num] == 0:
                    del freq_map[left_num]
                left += 1
            
       
            if right - left + 1 == k and len(freq_map) == k:
                max_sum = max(max_sum, current_sum)
                
        return max_sum