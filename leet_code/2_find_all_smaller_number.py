from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:


        sorted_num = sorted(nums)

        info = dict()



        for i,n in enumerate(sorted_num):
            print(i,n)

            if info.get(n,None) is None:
                info[n]=i

            
        ret = []

        for n in nums:
            ret.append(info[n])

        print(ret)


"""
[8,1,2,2,3]
"""


print(Solution().smallerNumbersThanCurrent(nums=[8,1,2,2,3]))