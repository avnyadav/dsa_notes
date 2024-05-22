import math

MOD_VAL = (10**9)+7

def func(n,dp):

        
    if n==1:
        return 0
    if n==2:
        return 1

    if dp[n]!=-1:
        return dp[n]
    
    n1=n-1
    n2=n-2

    ans = n1*((func(n2,dp)+func(n1,dp))%MOD_VAL)
    dp[n]=ans%MOD_VAL
    return dp[n]

def tabulation(n):
    if n==1:
        return 0
    if n==2:
        return 1

    first,second=0,1
    for i in range(3,n+1):
        total  = (first+second)%MOD_VAL
        ans = ((i-1)*total)%MOD_VAL
        first=second
        second=ans
    
    return second
    

def countDerangements(n):
    # Write your code here.
   
    dp =[-1]*(n+1)
    return tabulation(n)

# Main.
t = int(input())
while t:
    n = int(input())
    print(countDerangements(n))
    t = t-1