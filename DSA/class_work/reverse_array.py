class Solution:
    def reverseArray(self, arr):
        n = len(arr)
        
        for i in range(n//2):
            arr[i],arr[n-1-i]=arr[n-1-i],arr[i]
            
        return(arr)
        