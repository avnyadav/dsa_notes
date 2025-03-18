"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ""
        for r in range(numRows):
            increment = (numRows-1)*2
            for i in range(r,len(s),increment):
                res += s[i]
                if r>0 and r<numRows-1 and i+increment-2*r <len(s):
                    res += s[i+increment-2*r]
        return res
    

if __name__=="__main__":
    print(Solution().convert("PAYPALISHIRING",3))