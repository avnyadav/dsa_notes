from typing import List, Dict

class Solution:
    #only recursion
    def solve(self, cost: List[int], n: int, dp:Dict[int,int] ) -> int:
        #base case
        if n<=1:
            return cost[n]
        ans: int = cost[n] + min(self.solve(cost, n-1), self.solve(cost, n-2))
        return ans

    #recursion with memoization = dp
    def solve2(self, cost: List[int], n: int, dp:List[int] ) -> int:
        #base case
        if n==1:
            return cost[n]
        if n==0:
            return cost[n]
            
        if dp[n]!=-1:
            return dp[n]
        #step 2
        dp[n]: int = cost[n] + min(self.solve2(cost, n-1, dp), self.solve2(cost, n-2, dp))
        return dp[n]

    def solve3(self, cost: List[int]) -> int:
        dp:List[int] =[]
        dp.append(cost[0])
        dp.append(cost[1])
        n=len(cost)
        for i in range(2,n):
            dp.append(cost[i] + min(dp[i-1], dp[i-2]))
        
        return min(dp[n-1],dp[n-2])



    def solve4(self, cost: List[int]) -> int:
        c_prev_1=cost[0]
        c_prev_2=cost[1]
        n=len(cost)
        for i in range(2,n):
            c_current:int = cost[i] + min(c_prev_1, c_prev_2)
            c_prev_1=c_prev_2
            c_prev_2=c_current
            
        return min(c_prev_1,c_prev_2)

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # n=len(cost)
        # ans = min(self.solve(cost,n-1),self.solve(cost,n-2))
        # n=len(cost)
        # #step1 dp data storage
        # dp:List[int] = [-1]*(n+1)
        # ans = min(self.solve2(cost, n-1, dp), self.solve2(cost, n-2, dp))
        ans=  self.solve4(cost)
        return ans
    



        
        