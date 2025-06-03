from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l,u = 0,len(nums)-1

        while l<=u:
            mid = (l+u+1)//2

            if nums[mid]==target:
                return mid
            
            #Choose right second mean update left index to mid

            #left sorted portion
            if nums[l]<=nums[mid]:
                if target>nums[mid] or target<nums[l]:
                    l=mid+1
                else:
                    u=mid-1
            #right sorted portion
            else:
                if target<nums[mid] or target>nums[u]:
                    u=mid-1
                else:
                    l=mid+1
                    
        return -1

            

if __name__=="__main__":
    arr= [7,8,1,2,3,4,5,6]
    target = 2
    print(Solution().search(nums=arr,target=target))


