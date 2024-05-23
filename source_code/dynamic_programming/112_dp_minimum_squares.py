#User function Template for python3
import math



def solve(n,dp):
	if n==0:
	    return 0
    if dp[n]!=-1:
        return dp[n]
    ans = n
	i=1
	while i*i<=n:
	    ans = min(ans,1+solve(n-(i*i),dp))
	    i+=1
    dp[n]=ans
    return ans	    

def solve(n):
    dp=[float('inf')]*(n+1)
    dp[0]=0
    for i in range(1,n+1):
        j=1
        while j*j<=n:
            if i-(j*j)>=0:
                dp[i]=min(dp[i],1+dp[i-j*j])
            j+=1
    return dp[n]

class Solution:
	def MinSquares(self, n):
		# Code here 
	    dp = [-1]*(n+1)
	    return solve(n)
		