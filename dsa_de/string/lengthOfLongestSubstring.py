"""

3. Longest Substring Without Repeating Characters


Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

"""



class Solution:



    def lengthOfLongestSubstring(self, s: str) -> int:
        left_idx=0
        right_idx=0
        s_len= len(s)
        char_count = {}
        max_len = 0
        while left_idx<=right_idx and right_idx<s_len:
            #get current character and it's count
            char = s[right_idx]
            char_count[char]= char_count.get(char,0)+1
            n_count = char_count[char]
            while n_count!=1 and left_idx<=right_idx:
                char_count[s[left_idx]]=char_count.get(s[left_idx],0)-1
                left_idx+=1
                n_count=char_count.get(char,0)
            
            max_len = max(max_len,len(s[left_idx:right_idx+1]))
            right_idx+=1

        return max_len
            

    



if __name__=="__main__":
    text="pwwkew"
    print(Solution().lengthOfLongestSubstring(text))