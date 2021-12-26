class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        #3 -1   0  1
        #2 3 1 -1
        #1 -1. 2 -1
        #0   -1. 3 4
        
        nextStop = [(1,0),(-1,0),(0,1),(0,-1)]
        m,n = len(rooms),len(rooms[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j]==0:
                    q.append((i,j))
        while q:
            r,c = q.popleft()
            for x,y in nextStop:
                row = r+x
                col = c+y
                if(0 <= row < m and 0 <= col < n and rooms[row][col]==2147483647):
                    rooms[row][col] = rooms[r][c] + 1
                    q.append((row,col))
