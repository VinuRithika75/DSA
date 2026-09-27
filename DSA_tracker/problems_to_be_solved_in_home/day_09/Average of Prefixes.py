class Solution:
    def prefixAvg(self, arr):
        # code here
        prefix_sum = 0
        result = []

        for i in range(len(arr)):
            prefix_sum += arr[i]

            average = prefix_sum // (i + 1)

            result.append(average)

        return result