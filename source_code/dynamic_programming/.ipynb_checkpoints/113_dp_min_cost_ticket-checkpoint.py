from typing import List


def solve(n:int ,days:List[int], costs:List[int] ,index:int )->int:
    if index>=n:
        return 0

    # for 1 day
    d_cost_1 = costs[0] + solve(n, days, costs, index+1)

    days_limit = days[index]+7
    idx=index
    while idx<n and days[idx]< days_limit:
        idx+=1

    d_cost_7 = costs[1] + solve(n, days,costs,idx)

    days_limit = days[index]+30
    idx=index
    while idx<n and days[idx]< days_limit:
        idx+=1

    d_cost_30 = costs[2] + solve(n, days,costs,idx)
    
    return min(d_cost_1,d_cost_7,d_cost_30)


def solveMem(n:int ,days:List[int], costs:List[int] ,index:int ,dp)->int:
    if index>=n:
        return 0
    if dp[index]!=-1:
        return dp[index]
    # for 1 day
    d_cost_1 = costs[0] + solveMem(n, days, costs, index+1,dp)

    days_limit = days[index]+7
    idx=index
    while idx<n and days[idx]< days_limit:
        idx+=1

    d_cost_7 = costs[1] + solveMem(n, days,costs,idx, dp)

    days_limit = days[index]+30
    idx=index
    while idx<n and days[idx]< days_limit:
        idx+=1

    d_cost_30 = costs[2] + solveMem(n, days,costs,idx,dp)
    
    dp[index] =  min(d_cost_1,d_cost_7,d_cost_30)
    return dp[index]


def solveTab(n, days, costs):
    dp = [float('inf')]*(n+1)
    dp[n]=0
    for k in range(n-1,-1,-1):
        d_cost_1 = costs[0] + dp[k+1] #solveMem(n, days, costs, index+1,dp)

        days_limit = days[k]+7
        idx=k
        while idx<n and days[idx]< days_limit:
            idx+=1

        d_cost_7 = costs[1] + dp[idx]

        days_limit = days[k]+30
        idx=k
        while idx<n and days[idx]< days_limit:
            idx+=1

        d_cost_30 = costs[2] + dp[idx]
        dp[k] =  min(d_cost_1,d_cost_7,d_cost_30)
    
    return dp[0]




def minimumCoins(n, days, costs):
    # Write your code here.
    # dp=[-1]*(n+1)
    # return solveMem(n,days,costs,0,dp)
    return solveTab(n, days, costs)


