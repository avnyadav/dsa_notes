from typing import List

arr = [2,1,4,7,3,2,5]
def longest_mountain(arr:List[int]):

    n:int = len(arr)
    res=0
    for i in range(1,n-1):
        if arr[i-1] < arr[i] > arr[i+1]:
            l=r=i 
            while l>=0 and arr[l-1]<arr[l]:
                l-=1
            while r<n-1 and arr[r]>arr[r+1]:
                r+=1
            res = max(res,r-l+1)
    return res
            


print(longest_mountain(arr))
