class Solution:
    def rearrange(self,arr):
        # code here
        positive = []
        negative = []

        for x in arr:
            if x >= 0:
                positive.append(x)
            else:
                negative.append(x)

        p = 0
        n = 0
        index = 0

        while p < len(positive) and n < len(negative):
            arr[index] = positive[p]
            index += 1
            p += 1

            arr[index] = negative[n]
            index += 1
            n += 1

        while p < len(positive):
            arr[index] = positive[p]
            index += 1
            p += 1

        while n < len(negative):
            arr[index] = negative[n]
            index += 1
            n += 1

        print(arr)