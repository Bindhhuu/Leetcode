class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m= len(matrix)
        n= len(matrix[0])
        t= m*n
        l= 0
        r= t-1

        while l <= r:
            m= (l+r)//2
            i= m//n
            j= m%n
            mid= matrix[i][j]

            if mid== target:
                return True
            elif target < mid:
                r= m-1
            else:
                l= m+1
        return False
