from sys import *
from collections import *
from math import *


MOD = 10**9+7


def add(n1,n2):
    return ((n1%MOD)+(n2%MOD))%MOD

def mul(n1,n2):
    return ((n1%MOD)*(n2%MOD))%MOD    


def solve(n,k):
    if n==1:
        return k
    if n==2:
        return add(k,mul(k,k-1))
    
    ans =add(mul(solve(n-2,k),(k-1)),mul(solve(n-1,k),(k-1)))

    return ans

def solveMemoization(n,k,dp):
    if n==1:
        return k
    if n==2:
        return add(k,mul(k,k-1))
    if dp[n]!=-1:
        return dp[n]
    ans =add(mul(solveMemoization(n-2,k,dp),(k-1)),mul(solveMemoization(n-1,k,dp),(k-1)))
    dp[n]=ans
    return ans

def solveTab(n,k):
    if n==1:
        return k
    dp=[0]*(n+1)
    dp[1]=k

    dp[2]=add(k,mul(k,k-1))
    for i in range(3,n+1):
        dp[i]=add(mul(dp[i-2],k-1),mul(dp[i-1],k-1) )
    return dp[n]

def numberOfWays(n: int, k: int) -> int:
    # write your code here
    
    return solveTab(n,k)
    #pass