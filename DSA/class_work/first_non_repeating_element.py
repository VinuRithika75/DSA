class Solution:
    def firstNonRepeating(self, arr):
        count = {}

        for x in arr:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1

        for x in arr:
            if count[x] == 1:
                return x

        return 0