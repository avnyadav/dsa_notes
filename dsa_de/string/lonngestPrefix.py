from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest_str_len = min([ len(s) for s in strs])

        idx=0
        prefix=""
        while idx<smallest_str_len:
            for strs_idx in range(1,len(strs)):
                if strs[0][idx]!=strs[strs_idx][idx]:
                    return prefix
            prefix+=strs[0][idx]
            idx+=1
        return prefix
    
if __name__=="__main__":
    strs =["dog","racecar","car"]
    print(Solution().longestCommonPrefix(strs))