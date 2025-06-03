from typing import List


    


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction=1

        ret = []
        while matrix:
            
            if direction==1:
                items = matrix.pop(0)
                ret.extend(items)
                r=len(matrix)-1
                if r<0:
                    break
                c=len(matrix[0])-1
                for r in range(r+1):
                    ret.append(matrix[r].pop(c))
                
                direction=direction*-1

            if direction==-1:
                items = matrix.pop()
                ret.extend(items[::-1])

                r=len(matrix)-1
                c=0
                if r<0:
                    break
                for r in range(r,-1,-1):
                    ret.append(matrix[r].pop(c))


                direction=direction*-1
        
        return ret





class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret=[]

        while matrix:
            #add first row
            ret.extend(matrix.pop(0))

            #add last item of each row
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())
            
            #add last row
            if matrix:
                ret.extend(matrix.pop()[::-1])
            
            #add first element of each row from reverse order of row
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        



matrix=[[7],[9],[6]]


print(Solution().spiralOrder(matrix))






            







if __name__=="__main__":
    pass