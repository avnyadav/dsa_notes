from typing import List
class Solution:

    def threeSum(self, nums: List[int])->List[List[int]]:
        res = []
        #sort the array
        nums.sort()
        n = len(nums)
        for idx,num in enumerate(nums):
            
            #now due to sorted error it is not possible to obtain 0 sum 
            if nums[idx]>0:
                return res
            if idx>0 and num==nums[idx-1]:
                continue
            

            left_idx, right_idx=idx+1, n-1

            while left_idx<right_idx:
                total  = nums[idx]+nums[left_idx]+nums[right_idx]
                if total<0:
                    left_idx+=1
                elif total>0:
                    right_idx-=1
                else:
                    res.append([nums[idx],
                                nums[left_idx],
                                nums[right_idx]
                                ])
                    left_idx+=1
                    right_idx-=1


                    #one we find right number we will start with different number combination hence 
                    #moving left idx until we find different number
                    while left_idx<right_idx and nums[left_idx]==nums[right_idx]:
                        left_idx+=1
                    
        return res

if __name__=="__main__":
    nums = [-2,0,1,1,2]
    Solution().threeSum(nums)
