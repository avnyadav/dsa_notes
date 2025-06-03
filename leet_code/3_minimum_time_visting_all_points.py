from typing import List

class Solution:
    
    def get_max_diff(self,p1,p2):
        x_diff = abs(p1[0]-p2[0])
        y_diff = abs(p1[1]-p2[1])
        return max(x_diff,y_diff)



    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        curr_sec = 0

        for idx in range(1,len(points)):
            curr_sec += self.get_max_diff(points[idx],points[idx-1])
        return curr_sec
    

if __name__=="__main__":
    points = [[1,1],[3,4],[-1,0]]
    print(Solution().minTimeToVisitAllPoints(points))