
grid = [[".",".", "#", "#"],
        ["#",".", "#", "#"],
        ["#",".", ".", "."]
        ]
rows = len(grid)
cols = len(grid[0])
grid2 = [[1]*(cols+1) for _ in range(rows+1)]

for i in range(rows+1):
    for j in range(cols+1):
        if i == rows or j == cols:
            grid2[i][j] = float("inf")
grid2[rows][cols-1] = 0


for i in range(rows-1,-1,-1):
    for j in range(cols-1,-1,-1):
        if grid[i][j] == ".":
            grid2[i][j] = min(grid2[i][j+1]+grid2[i][j], grid2[i+1][j]+grid2[i][j])
        else:
            grid2[i][j] = float('inf')
            
print(grid2[0][0]-1)
