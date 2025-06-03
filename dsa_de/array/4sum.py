from typing import List

class Solution:

    def fourSum(self, nums:List[int], target:int)->List[List[int]]:
        nums.sort()
        res = []
        quad = []

        def helper(k,start, target):
            if k!=2:

                # choose one item search from 
                # next item for remaning sum
                for i in range(start, len(nums)-k+1):

                    #skip duplicates
                    if i>start and nums[i]==nums[i-1]:
                        continue

                    quad.append(nums[i])
                    helper(k-1, i+1, target-nums[i])
                    quad.pop()
                return


                
            l,r = start, len(nums)-1

            while l<r:

                total = nums[l] + nums[r]

                if total<target:
                    l+=1
                
                elif total>target:
                    r-=1
                
                else:
                    res.append(quad+[nums[l], nums[r]])

                    l+=1
                    #moving left pointer to next until different item found
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
            
        helper(4, 0,target)
        return res
    

print(Solution().fourSum(nums=[2,2,2,2,2], target=8))
                




