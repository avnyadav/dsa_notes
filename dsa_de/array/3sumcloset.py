from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        ans=None
        diff = float('inf')

        resSum=0
        for idx  in range(n):
            if idx>0 and nums[idx]==nums[idx-1]:
                continue
            
            l,r = idx+1, n-1

            while l<r:

                total = nums[idx]+nums[l]+nums[r]

                if total<target:
                    l+=1
                elif total>target:
                    r-=1
                else:
                    return total
                
                diffToUpdate  = abs(total-target)
                if diffToUpdate<diff:
                    resSum=total
                    diff=diffToUpdate
        return resSum


if __name__=="__main__":
    arr = [-1,2,1,-4]

    print(Solution().threeSumClosest(nums=arr,target=1))