nums = [0,1]


def subsets(nums):
    res = []
    def backtrack(sub:list=[],i=0):
        if i==len(nums):
            res.append(sub)
            return
        backtrack(sub,i+1)
        backtrack(sub+[nums[i]],i+1)
    backtrack()
    return res 



res = subsets(nums)
print(res)