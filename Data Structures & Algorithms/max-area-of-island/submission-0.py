class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0 

        def dfs(row,col):
            nonlocal temp
            grid[row][col] = 0

            if row>0 and grid[row-1][col] ==1:
                temp+=1
                dfs(row-1,col)
            if row<rows-1 and grid[row+1][col] ==1:
                temp+=1
                dfs(row+1,col)
            if col>0 and grid[row][col-1] ==1:
                temp+=1
                dfs(row,col-1)
            if col<cols-1 and grid[row][col+1] ==1:
                temp+=1
                dfs(row,col+1)

        for row in range(rows):
            for col in range(cols):
                temp = 0 
                if grid[row][col]==1:
                    temp+=1
                    dfs(row,col)
                max_area = max(max_area,temp)


        return max_area