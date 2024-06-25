from typing import List

from bisect import bisect_left
def solve(envelopes):
    n = len(envelopes)
    if n==0:
        return 0
    sort_envelopes=sorted(envelopes,key= lambda x: (x[0],-x[1]))
    ans =[sort_envelopes[0][1]]
    for i in range(1,n):
        if sort_envelopes[i][1]>ans[-1]:
            ans.append(sort_envelopes[i][1])
        else:
            replace_idx= bisect_left(ans,sort_envelopes[i][1])
            ans[replace_idx]=sort_envelopes[i][1]
    return len(ans)

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        return solve(envelopes)
        