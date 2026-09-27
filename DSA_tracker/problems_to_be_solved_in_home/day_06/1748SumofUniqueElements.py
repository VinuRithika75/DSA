class Solution:
    def sumOfUnique(self, nums):
        count = {}

        for x in nums:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1

        total = 0

        for x in nums:
            if count[x] == 1:
                total += x

        return total