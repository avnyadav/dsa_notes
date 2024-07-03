from typing import List
def solveTab(index:int, diff:int, arr:List[int], dp):
    if index<0:
        return 0
        
    ans = 0
    if dp[index].get(diff,None):
        return dp[index][diff]
    for j in range(index-1, -1, -1):
        if arr[index]-arr[j] == diff:
            ans = max(ans, 1 + solveTab(index=j, diff=diff, arr=arr, dp=dp))
    
    dp[index][diff]=ans
    return dp[index][diff]

    
class Solution:
    def lengthOfLongestAP(self, A, n):
        # code here
        #if array has less than 2 element ap will be of same size as array
        if n <= 2:
            return n
            
        ans = 0
        dp = [dict() for i in range(n+1)]
        for i in range(n):
            for j in range(i+1, n):
                ans = max(ans, 2 + solveTab(index=i, diff=A[j]-A[i], arr=A, dp=dp))
        
        return ans
    

if __name__=="__main__":
    s = Solution()
    A = [1,4,6,8]
    s.lengthOfLongestAP(A,len(A))