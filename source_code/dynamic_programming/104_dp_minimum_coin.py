from os import *
from sys import *
from collections import *
from math import *

from typing import List

INT_MAX = float('inf')


def solveRec(num,x,dp):
    if x==0:
        return 0
    if x<0:
        return INT_MAX
    mini=INT_MAX
    if dp[x]!=-1:
        return dp[x]

    for coin in num:
        ans =  solveRec(num,x-coin,dp)
        if ans!=INT_MAX:
            mini = min(1+ans,mini)
    dp[x]=mini
    return mini



def solveTab(num,x):
    dp=[INT_MAX]*(x+1)
    dp[0]=0
    for i in range(1,x+1):
        for coin in num: 
            if i-coin>=0 and dp[i-coin]!=INT_MAX:
                dp[i]=min(dp[i], 1+ dp[i-coin])
    
    if dp[x]==INT_MAX:
        return -1
    return dp[x]

def minimumElements(num: List[int], x: int) -> int:
    # # Write your code here.
    # dp = [-1]*(x+1)
    # ans = solveRec(num,x,dp)

    # if ans==INT_MAX:
    #     return -1
    ans=  solveTab(num,x)
    return ans