"""
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution:
    

    def searchPalindrome(self,s,l,r,res,resLen):

        while l>=0 and r<len(s) and s[l]==s[r]:
            if (r-l+1)>resLen:
                res=s[l:r+1]
                resLen=r-l+1
            l-=1
            r+=1
        return res,resLen

    def longestPalindrome(self, s: str) -> str:
        
        res=""
        resLen=0
        for i in range(len(s)):

            #odd scenario
            l,r=i,i
            res,resLen=self.searchPalindrome(s,l,r,res,resLen)
            l,r=i,i+1
            res,resLen=self.searchPalindrome(s,l,r,res,resLen)
            
        return res,resLen


if __name__=="__main__":
    print(Solution().longestPalindrome(s=input("Enter text:\n")))