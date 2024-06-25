from typing import List

class Solution:
    
    def solve(self,statisfaction: List[int], t, n,stsIdx):
        #all dishesh calculated
        if stsIdx==n:
            return 0

        #include = 
        inc = statisfaction[stsIdx]*t+self.solve(statisfaction,t+1,n,stsIdx+1)
        #exclude = 
        exc = self.solve(statisfaction,t,n,stsIdx+1)

        return max(inc,exc)

    def solveMem(self,statisfaction: List[int], t, n,stsIdx,dp):
        #all dishesh calculated
        if stsIdx==n:
            return 0
        if dp[stsIdx][t]!=-1:
            return dp[stsIdx][t]
        #include = 
        inc = statisfaction[stsIdx]*t+self.solveMem(statisfaction,t+1,n,stsIdx+1,dp)
        #exclude = 
        exc = self.solveMem(statisfaction,t,n,stsIdx+1,dp)

        dp[stsIdx][t] =  max(inc,exc)
        return dp[stsIdx][t]
    

    def solveTab(self,satisfaction):
        n = len(satisfaction)
        dp = [[0 for i in range(0,n+1)] for i in range(0,n+1) ]

        for stsIdx in range(n-1,-1,-1):
            for time in range(stsIdx,-1,-1):
                inc = satisfaction[stsIdx]*(time+1)+dp[stsIdx+1][time+1]
                exc = dp[stsIdx+1][time]
                dp[stsIdx][time]=max(inc,exc)

        return dp[0][0]




    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n=len(satisfaction)
        dp = [[-1 for i in range(0,n+1)] for i in range(0,n+1) ]
        #return self.solveMem(statisfaction=satisfaction, t=1,n=n,stsIdx=0,dp=dp)
        return self.solveTab(satisfaction=satisfaction)
    
if __name__=="__main__":
    Solution().maxSatisfaction(satisfaction=[2,3,4])
        