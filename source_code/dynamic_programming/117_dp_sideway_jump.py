import copy
from typing import List
class Solution:


    def solve(self, obstacles: List[int]) -> int:
        n:int = len(obstacles)-1
        curr:List[int] = [float('inf')]*4
        _next:List[int] = [0]*4

        '''
        I will start from second last index
        ''' 
        for currPos in range(n-1,-1,-1):
            '''
            checking for each lane
            '''
            for currlane in range(1,4):

                if obstacles[currPos+1]!=currlane:
                    curr[currlane] = _next[currlane]
                else:
                    ans = float('inf')
                    for lane in range(1,4):
                        if currlane!=lane and obstacles[currPos]!=lane:
                            ans = min(ans, 1+ _next[lane])
                    
                    curr[currlane] = ans
            _next = copy.deepcopy(curr)
        ans = min(_next[1]+1,_next[2],_next[3]+1)
        return ans






    def minSideJumps(self, obstacles: List[int]) -> int:
        return self.solve(obstacles)
        