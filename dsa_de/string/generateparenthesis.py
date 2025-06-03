from typing import List
class Solution:

    def generateParenthesis(self, n:int)->List[str]:


        res=[]
        g_prth = ""
        def backTrack(openN, closeN,g_prth):

            if openN==closeN and openN==n:
                res.append(g_prth)
                return
            
            if openN<n:
                g_prth=f"{g_prth}("
                backTrack(openN+1, closeN, g_prth)
                g_prth=g_prth[:len(g_prth)-1]
            if closeN<openN:

                g_prth=f"{g_prth})"
                backTrack(openN,closeN+1, g_prth)
                g_prth = g_prth[:len(g_prth)-1]
        backTrack(0,0,g_prth)
        return res
    
print(Solution().generateParenthesis(3))