grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]


from typing import List
import collections
class Solution():

    def num_islands(self, grid:List[List[str]])->int:
        #if grid is empty
        if not grid:
            return 0
        
        visit = set()
        islands:int = 0
        rows,cols = len(grid),len(grid[0])


        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))

            while q:
                row, col =q.popleft()
                directions = [
                    [1,0], #right
                    [-1,0],#left
                    [0,1], #up
                    [0,-1] #down
                              ] 
                for dr,dc in directions:
                    r, c = row+dr, col+dc 
                    if (r in range(rows) and 
                        c in range(cols) and 
                        grid[r][c]=="1" and 
                        (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    islands+=1
        return islands
    

print("Number of Island",Solution().num_islands(grid))
