INT_MIN = float('-inf')
def solveRec(n,x,y,z,dp):
    if n==0:
        return 0
    if n<0:
        return INT_MIN

    if dp[n]!=-1:
        return dp[n]

    x_ans = solveRec(n-x,x,y,z,dp)+1 
    y_ans = solveRec(n-y,x,y,z,dp)+1 
    z_ans = solveRec(n-z,x,y,z,dp)+1 

    ans = max(x_ans,y_ans,z_ans)
    dp[n]=ans
    return dp[n]


def solvetab(n,x,y,z):
    dp=[INT_MIN]*(n+1)
    dp[0]=0
    for i in range(1,n+1):
        if  i-x>=0:
            dp[i]=max(dp[i],dp[i-x]+1)
        if  i-y>=0:
            dp[i]=max(dp[i],dp[i-y]+1)
        if  i-z>=0:
            dp[i]=max(dp[i],dp[i-z]+1)


    if dp[n]<0:
        return 0
    return dp[n]


def cutSegments(n, x, y, z):
    # Write your code here.
    # dp=[-1]*(n+1)
    # ans  =  solveRec(n,x,y,z,dp)
    # if ans==INT_MIN:
    #     return 0
    # return ans
    return solvetab(n,x,y,z)
    