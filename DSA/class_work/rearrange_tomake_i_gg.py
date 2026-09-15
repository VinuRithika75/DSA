class Solution:

    def modifyArray(self, arr):
        #code here

        n = len(arr)

        for i in range(n):
            if arr[i] != -1:
                value = arr[i]
                arr[i] = -1

                while value != -1:
                    next_value = arr[value]
                    arr[value] = value
                    value = next_value

        print(arr)