def occur(size,numbers,target):
    l = 0
    r = len(numbers)-1
    first = 0
    last = 0
    while l < r:
        if numbers[l]==target:
            first = l
        else:
            l+=1
        if numbers[r]==target:
            last = r
        else:
            r-=1
    print(first, last)