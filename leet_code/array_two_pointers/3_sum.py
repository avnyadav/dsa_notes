nums = [-1,0,1,2,-1,-4]

from typing import List

class Solution:

    def three_sum(self, nums: List[int]):
        
        nums.sort()
        res = []
        n = len(nums)
        for idx,num in enumerate(nums):

            if num>0:
                return res
            
            if idx>0 and num ==nums[idx-1]:
                continue

            left_idx, right_idx = idx+1, n-1

            while left_idx<right_idx:
                total = num+nums[left_idx]+nums[right_idx]

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
                    while left_idx<right_idx and nums[left_idx]==nums[left_idx-1]:
                        left_idx+=1
                    
        return res
    


     







if __name__=="__main__":

    Solution().three_sum(nums)