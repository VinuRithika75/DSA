class Solution:
    def arrange(self,arr): 
        #code here

        n = len(arr)

        for i in range(n):
            arr[i] = arr[i] + (arr[arr[i]] % n) * n

        for i in range(n):
            arr[i] = arr[i] // n

        print(arr)