from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

def solve(nums,n,dp):
    if n<0:
        return 0
    if n==0:
        return nums[0]
    if dp[n]!=-1:
        return dp[n]
    include = solve(nums,n-2,dp)+nums[n]
    exclude = solve(nums,n-1,dp)+0
    dp[n] =  max(include,exclude)
    return dp[n]


def solveTab(nums):
    n=len(nums)
    dp=[0]*n
    dp[0]=nums[0]
    for i in range(1,n):
    
        incl = dp[i-2]+nums[i]
        excl = dp[i-1]+0
        dp[i]=max(incl,excl)
    
    return dp[n-1]

def maximumNonAdjacentSum(nums):    
    # Write your code here.
    # dp=[-1]*len(nums)
    return solveTab(nums)

# Main.
t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    
    t -= 1