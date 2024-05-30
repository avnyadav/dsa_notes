from typing import List
class Solution:
    
    def solve(self, values: List[int], startIdx:int, endIdx:int)->int:

        if startIdx+1==endIdx:
            return 0
        ans = float('inf')
        for i in range(startIdx+1,endIdx):
            ans = min(ans,   (values[startIdx] * values[i] * values[endIdx]) + self.solve(values, startIdx,i)
            + self.solve(values, i, endIdx))
        
        return ans

    def solveMem(self, values: List[int], startIdx:int, endIdx:int)->int:

        if startIdx+1==endIdx:
            return 0

        if self.dp[startIdx][endIdx]!=-1:
            return self.dp[startIdx][endIdx]

        ans = float('inf')
        for i in range(startIdx+1,endIdx):
            ans = min(ans,   (values[startIdx] * values[i] * values[endIdx]) + self.solve(values, startIdx,i)
            + self.solve(values, i, endIdx))
        self.dp[startIdx][endIdx]=ans
        return ans

    # def solveTab(self,v):
    #     n:int  = len(v)
    #     dp: List[List[int]] = [[0]*n]*n
        
    #     for sIdx in range(n-1,-1,-1):
    #         for eIdx in range(sIdx+2,n):
    #             ans = float('inf')
    #             for mIdx in range(sIdx+1,eIdx):
    #                 ans = min(ans, (v[sIdx]*v[mIdx]*v[eIdx])+ dp[sIdx][mIdx]+dp[mIdx][eIdx])
    #             dp[sIdx][eIdx]=ans
        
    #     return dp[0][n-1]



    def solveTab(self,v):
        n:int  = len(v)
        dp: List[List[int]] = [[0]*n]*n

        for startIdx in range(0,n-3):
            for endIdx in range(startIdx+2,n):
                ans= float('inf')
                for mIdx in range(startIdx+1,endIdx):
                    ans = min( ans, v[startIdx]*v[mIdx]*v[endIdx]+ dp[startIdx][mIdx]+dp[mIdx][endIdx])
                dp[startIdx][endIdx]=ans
        
        return dp[n-4][n-2]
    
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        return self.solveTab(values)
   