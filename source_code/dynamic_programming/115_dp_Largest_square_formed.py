
from typing import List


    
class Solution:
    
    
    def solve(self,row,col,mat):
    
        #base case if matrix length exceed
        if row>=len(mat) or col>=len(mat[0]):
            return 0
            
        #check for right
        right = self.solve(row,col+1,mat)
        
        #check for diagonal
        diagonal  = self.solve(row+1,col+1,mat)
        
        #check for down
        down = self.solve(row+1,col,mat)
        
        if mat[row][col]==0:
            return 0

        ans =  1 + min(right,diagonal,down)
        self.maxi = max(ans,self.maxi)
        return ans
    
    
    
    def solveMem(self,row,col,mat):
    
        #base case if matrix length exceed
        if row>=len(mat) or col>=len(mat[0]):
            return 0
            
        if self.dp[row][col]!=-1:
            return self.dp[row][col]
            
        #check for right
        right = self.solveMem(row,col+1,mat)
        
        #check for diagonal
        diagonal  = self.solveMem(row+1,col+1,mat)
        
        #check for down
        down = self.solveMem(row+1,col,mat)
        
        if mat[row][col]==0:
            self.dp[row][col]=0
            return 0

        ans =  1 + min(right,diagonal,down)
        self.maxi = max(ans,self.maxi)
        self.dp[row][col]=ans
        return ans
    
    
    
    def maxSquare(self, n : int, m : int, mat : List[List[int]]) -> int:
        # code here
        self.maxi=0
        self.dp=[[-1]*m]*n
        
        self.solveMem(0,0,mat)
        return self.maxi


#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n, m = map(int, input().split())

        mat = IntMatrix().Input(n, m)

        obj = Solution()
        res = obj.maxSquare(n, m, mat)

        print(res)

# } Driver Code Ends