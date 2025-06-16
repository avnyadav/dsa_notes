class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leftWindow=0
        charCount = {}
        longestSubstring=0
        for rightWindow in range(len(s)):
            charCount[s[rightWindow]]=charCount.get(s[rightWindow],0)+1
            #charcter is repeating
            if charCount[s[rightWindow]]==1:
                longestSubstring=max(longestSubstring,rightWindow-leftWindow+1)
            while charCount[s[rightWindow]]!=1 and leftWindow<rightWindow:
                charCount[s[leftWindow]]-=1
                leftWindow+=1
        print(f"Longest substring {longestSubstring}")
        return longestSubstring


if __name__=="__main__":
    Solution().lengthOfLongestSubstring("abcabcbb")