class Solution(object):
    def maxSlidingWindow(self, nums, k):
        result = []

        for i in range(len(nums) - k + 1):
            window = nums[i:i+k]
            result.append(max(window))

        return result