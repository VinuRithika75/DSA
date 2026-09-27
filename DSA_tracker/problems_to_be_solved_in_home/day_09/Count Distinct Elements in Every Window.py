class Solution:
    def countDistinct(self, arr, k):
        n=len(arr)
        result = []

        for i in range(n- k + 1):
            window = arr[i:i + k]
            distinct_count = len(set(window))
            result.append(distinct_count)

        return result