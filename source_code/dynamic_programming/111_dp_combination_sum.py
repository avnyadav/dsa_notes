from os import *
from sys import *
from collections import *
from math import *

from typing import List


def solve(num,tar,dp):
    if tar==0:
        return 1

    if tar<0:
        return 0

    if dp[tar]!=-1:
        return dp[tar]
        
    total = 0
    for n in num:
        total+=solve(num,tar-n,dp)
    dp[tar]=total
    return total


def solveTab(num,tar):
    dp = [0]*(tar+1)
    dp[0]=1
    for i in range(1,tar+1):
        for n in num:
            if i-n>=0:
                dp[i]+=dp[i-n]
    return dp[tar]



def findWays(num: List[int], tar: int) -> int:
    # Write your code here.
    # dp = [-1]*(tar+1)
    # return solve(num,tar,dp)
    return solveTab(num,tar)