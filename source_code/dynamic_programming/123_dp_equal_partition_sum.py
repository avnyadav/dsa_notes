# User function Template for Python3
import copy
def solve(target, arr, idx, N ):
    if idx>=N:
        return False
    if target==0:
        return True
    if target<0:
        return False
    
    inc = solve(target-arr[idx],arr,idx+1,N)
    exc = solve(target,arr,idx+1,N)
    return inc or exc
    
    
def solveMem(target, arr, idx, N ,dp):
    if idx>=N:
        return False
    if target==0:
        return True
    if target<0:
        return False
    if dp[target][idx]!=-1:
        return dp[target][idx]
    
    inc = solveMem(target-arr[idx],arr,idx+1,N,dp)
    exc = solveMem(target,arr,idx+1,N,dp)
    status =  inc or exc
    dp[target][idx]=status
    return dp[target][idx]
    
    
    
def solvetab(arr, N , target):
    dp = [[0 for j in range(target+1)] for i in range(N+1)]
    
    for i in range(N+1):
        dp[i][0]=1
    
    for idx in range(N-1,-1,-1):
        for t in range(target+1):
            #inc = solveMem(target-arr[idx],arr,idx+1,N,dp)
            inc =0
            if target-arr[idx]>=0:
                inc  = dp[idx+1][t-arr[idx]]
            #exc = solveMem(target,arr,idx+1,N,dp)
            exc = dp[idx+1][t]
            status =  inc or exc
            dp[idx][t]=status
    
    return dp[0][target]


def solvetabSO(arr, N , target):
    dp = [[0 for j in range(target+1)] for i in range(N+1)]
    
    curr = [0 for i in range(target+1)]
    curr[0]=1
    next_ = [0 for j in range(target+1)]
    next_[0]=1

    for i in range(N+1):
        dp[i][0]=1
    
    for idx in range(N-1,-1,-1):
        for t in range(target+1):
            #inc = solveMem(target-arr[idx],arr,idx+1,N,dp)
            inc =0
            if target-arr[idx]>=0:
                inc  = next_[t-arr[idx]]
            #exc = solveMem(target,arr,idx+1,N,dp)
            exc = next_[t]
            status =  inc or exc
            curr[t]=status
        next_ = copy.deepcopy(curr)
    return next_[target]
                    
                    
            
    


class Solution:
    def equalPartition(self, N, arr):
        # code here
        
        total = sum(arr)
        if total%2!=0:
            return 0
        target = total//2
        dp = [[-1 for i in range(N+1)] for j in range(target+1)]
        # status = solveMem(target, arr, 0,N, dp)
        status = solvetab(arr, N, target)
        if status:
            return 1
        return 0
       

#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends