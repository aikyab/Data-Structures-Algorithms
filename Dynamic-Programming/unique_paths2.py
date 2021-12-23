class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        #0 0 0
        #0 1 0
        #0 0 0
        #Approach 1 Bottom Up Dp array
        if obstacleGrid[0][0]==1:
            return 0
        rows,columns = len(obstacleGrid),len(obstacleGrid[0])
        obstacleGrid[0][0] = 1
        for j in range(1,columns):
            obstacleGrid[0][j] = int(obstacleGrid[0][j]==0 and obstacleGrid[0][j-1]==1)
        for i in range(1,rows):
            obstacleGrid[i][0] = int(obstacleGrid[i][0]==0 and obstacleGrid[i-1][0]==1)
        
        for i in range(1,rows):
            for j in range(1,columns):
                if obstacleGrid[i][j]==0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
                    
        return obstacleGrid[rows-1][columns-1]

#         #Approach 2 Top Down Recursive
#         if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
#             return 0
#         def dfs(grid,i,j,m,n,seen):
#             key = str(i)+","+str(j)
#             if key in seen:
#                 return seen[key]
#             if i==m and j==n:
#                 if grid[i][j]==0:
#                     return 1
#                 return 0
#             if i>m or j>n:
#                 return 0
#             if grid[i][j]==1:
#                 return 0
#             left = dfs(grid,i+1,j,m,n,seen)
#             right = dfs(grid,i,j+1,m,n,seen)
#             seen[key] = left+right
#             return seen[key]
        
#         return dfs(obstacleGrid,0,0,len(obstacleGrid)-1,len(obstacleGrid[0])-1,{})
