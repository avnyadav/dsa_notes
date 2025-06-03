
from typing import List
class Solution:

    def letterCombination(self, digits:str)->List[str]:
        res=[]

        numToCharMap = {
                        "2":"abc",
                        "3":"def",
                        "4":"ghi",
                        "5":"jkl",
                        "6":"mno",
                        "7":"pqrs",
                        "8":"tuv",
                        "9":"wxyz"
                        }


        def backTrack(digitIdx,currStr):
            if len(currStr)==len(digits):
                res.append(currStr)
                return
            for c in numToCharMap[digits[digitIdx]]:
                backTrack(digitIdx+1,currStr+c)
        
        if digits!="":
            backTrack(0,"")
        return res

if __name__=="__main__":
    print(Solution().letterCombination("234"))