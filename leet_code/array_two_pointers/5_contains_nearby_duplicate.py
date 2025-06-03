from typing import List
nums = [1,2,3,1,2,3]
k = 3

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])

            if len(seen)>k:
                seen.remove(nums[i-k])
        
        return False






print(Solution().containsNearbyDuplicate(nums=nums,k=k))
        