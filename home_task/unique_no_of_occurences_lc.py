class Solution:
    def uniqueOccurrences(self, arr):
        count = {}

        for x in arr:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1

        seen = []

        for x in count:
            if count[x] in seen:
                return False
            seen.append(count[x])

        return True