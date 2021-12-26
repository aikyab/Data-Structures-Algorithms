class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix),len(matrix[0])
        left = 0
        right = m*n - 1
        
        while left<=right:
            mid = left + (right-left)//2
            i,j = mid//n,mid%n
            if target==matrix[i][j]:
                return True
            if target<matrix[i][j]:
                right = mid-1
            else:
                left = mid+1
        return False
                
            
