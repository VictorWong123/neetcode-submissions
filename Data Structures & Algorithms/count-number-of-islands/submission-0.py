class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0 

        def dfs(row,col):
            nonlocal rows, cols
            grid[row][col]="0"

            if row> 0 and grid[row-1][col] =="1":
                dfs(row-1,col)
            if row< rows-1 and grid[row+1][col] =="1":
                dfs(row+1,col)
            if col> 0 and grid[row][col-1] =="1":
                dfs(row,col-1)
            if col< cols-1 and grid[row][col+1] =="1":
                dfs(row,col+1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=="1":
                    dfs(row,col)
                    count +=1

        return count
