from os import *
from sys import *
from collections import *
from math import *
from typing import List
def solve(valueInHouse):
    n:int = len(valueInHouse)
    dp:List[int] = [0]*n
    dp[0]=valueInHouse[0]
    for i in range(1,n):
        inc = dp[i-2]+valueInHouse[i]
        excl = dp[i-1]
        dp[i]=max(inc,excl)
        
    return dp[n-1]

def houseRobber(valueInHouse):
    n=len(valueInHouse)
    if n==1:
        return valueInHouse[0]
    
    r1 = solve(valueInHouse[1:])
    r2 = solve(valueInHouse[:len(valueInHouse)-1])
    if r1>r2:
        return r1
    return r2